import sys
import datetime
from tkinter import Tk, filedialog
from functions.ai import *
from objects.button import *
from objects.chessboard import Chessboard
from objects.pieces import *

"""
	PRINCIPAL (INTERFAZ GRÁFICA)
"""

# GUI.
logo = pygame.image.load("resources/logo32x32.png")
pygame.init()
pygame.font.init()  # for text
background = pygame.image.load("resources/background.jpg")
font = pygame.font.SysFont("dejavuserif", 30)
pygame.display.set_icon(logo)
pygame.display.set_caption("Chess Finals")
screen = pygame.display.set_mode((1000, 600))
chessboard_background = pygame.image.load("resources/gui_board.png").convert()

reset = pygame.image.load("resources/buttons/reset.png")
reset_hover = pygame.image.load("resources/buttons/reset_hover.png")
load = pygame.image.load("resources/buttons/load.png")
load_hover = pygame.image.load("resources/buttons/load_hover.png")
new = pygame.image.load("resources/buttons/new.png")
new_hover = pygame.image.load("resources/buttons/new_hover.png")
casual = pygame.image.load("resources/buttons/casual.png")
finals = pygame.image.load("resources/buttons/finals.png")

# Variables.
chessboard = Chessboard()
clock = pygame.time.Clock()
board_width = 600
board_height = 600
column_margin = 30
row_margin = 60

# Botones.
reset_button = Button(x_offset=board_width + column_margin + 30, y_offset=30, width=150, height=30)
load_button = Button(x_offset=board_width + column_margin + 30, y_offset=80, width=150, height=30)
new_button = Button(x_offset=board_width + column_margin + 30, y_offset=130, width=150, height=30)
ia_mode_button = Button(x_offset=board_width + column_margin + 30, y_offset=180, width=150, height=30)

# Inicialización y carga de celdas para los eventos de interfaz gráfica.
sprite_group = pygame.sprite.Group()
sprite_array = [piece for row in chessboard.matrix for piece in row if piece]
sprite_group.add(sprite_array)
sprite_group.draw(screen)


# Función que se encarga de recuperar las coordenadas donde el mouse hace click y así recuperar (mediante la división)
# la posición exacta en la matriz de piezas (chessboard).
def select_cell():
	x, y = pygame.mouse.get_pos()
	return y // 70, x // 70


# Función que se encarga de recorrer el arreglo de objetos Sprite para recuperar una pieza seleccionada por color.s
def select_piece(color):
	actual_position = pygame.mouse.get_pos()
	cell_is_piece_selected = [s for s in sprite_array if s.rect.collidepoint(actual_position)]
	if len(cell_is_piece_selected) == 1 and cell_is_piece_selected[0].get_color() == color:
		cell_is_piece_selected[0].select()
		return cell_is_piece_selected[0]


# Función que escribe un mensaje de texto al lado derecho que muestra eventos del juego.
def game_message(message, colour):
	screen.blit(background, (600, 0))
	text = message.splitlines()
	index = 0
	for char in text:
		textsurface = font.render(char, False, colour)
		screen.blit(textsurface, (board_width + column_margin + 30, 450 + index))
		index += 28


# Función para recarga de interfaz.
def reload():
	global chessboard, sprite_array, sprite_group
	chessboard = Chessboard()
	sprite_group = pygame.sprite.Group()
	sprite_array = [piece for row in chessboard.matrix for piece in row if piece]
	sprite_group.add(sprite_array)
	sprite_group.draw(screen)


# Función que carga una partida prestablecida.
def load_game(filename):
	global chessboard, sprite_array, sprite_group
	chessboard = Chessboard(filename)
	sprite_group = pygame.sprite.Group()
	sprite_array = [piece for row in chessboard.matrix for piece in row if piece]
	sprite_group.add(sprite_array)
	sprite_group.draw(screen)


# Función principal.
# noinspection PyBroadException,PyShadowingNames
def main():
	screen.blit(background, (560, 0))
	player = "human"
	is_game_over = False
	is_piece_selected = False
	is_in_check = False
	final_file_name = ""
	ia_mode = "casual"
	game_message('Turno actual:\nJugador', (255, 255, 255))
	moves = 0

	# Ciclo de juego.
	while not is_game_over:

		# Movimientos de la IA.
		if player == "AI":

			# Recupera los movimientos del algoritmo minmax alfabeta co una profundidad por defecto de 4.
			# Si se aumenta la profundidad, el algoritmo tarda más en responder con el movimiento.
			if ia_mode == "casual":
				generated_value, ia_selected_move = minimax(chessboard, 4, float("-inf"), float("inf"), True, dict(), False)
			else:  # ia_mode == "finals"
				generated_value, ia_selected_move = minimax(chessboard, 8, float("-inf"), float("inf"), True, dict(), True)

			# Verificación para saber si el jugador ha ganado la partida.
			if generated_value == float("-inf") and ia_selected_move == 0:
				is_game_over = True
				player = "human"
				game_message('Jaque Mate:\nJugador gana', (255, 255, 0))

			# Movimientos realizados por el algoritmo de computadora (IA).
			else:
				start = ia_selected_move[0]
				end = ia_selected_move[1]
				piece = chessboard.matrix[start[0]][start[1]]
				kill_piece = chessboard.matrix[end[0]][end[1]]
				# Selección de la pieza, recupera las coordenadas de la celda para procesar el movimiento.
				piece_next_cell = chessboard.move_piece(piece, end[0], end[1])
				piece.focus_moved()

				# Si es un peón, rey o torre necesito marcarlo como movido
				if isinstance(piece, Pawn) or isinstance(piece, Rook) or isinstance(piece, King):
					piece.moved = True

				if piece_next_cell:
					sprite_group.add(piece_next_cell[0])
					sprite_array.append(piece_next_cell[0])
					sprite_group.remove(piece_next_cell[1])
					sprite_array.remove(piece_next_cell[1])

				# Remueve de los objetos la pieza eliminada.
				if kill_piece:
					sprite_group.remove(kill_piece)
					sprite_array.remove(kill_piece)
					chessboard.score += chessboard.piece_values[type(kill_piece)]

				# Verifica si el jugador se encuentra en jaque por la IA.
				player = "human"
				attacked = move_gen(chessboard, "b", True)
				king = chessboard.get_king('w')
				if (king.y, king.x) in attacked:
					game_message('Turno actual:\nJugador, en jaque', (255, 0, 0))
					is_in_check = True
				else:
					game_message('Turno actual:\nJugador', (255, 255, 255))
					is_in_check = False
				moves += 1
				chessboard.save_current_status(moves, piece, start, True)

			# Verifica si la IA gana la partida.
			if generated_value == float("inf"):
				is_game_over = True
				player = 'AI'
				game_message('Jaque mate:\nIA gana', (255, 255, 0))

		# Movimientos de la persona.
		# Se toma al jugador humano con el color blanco por defecto.
		elif player == "human":
			for event in pygame.event.get():
				mouse = pygame.mouse.get_pos()

				if event.type == pygame.QUIT:
					sys.exit()

				# Evento de click en pantalla.
				if event.type == pygame.MOUSEBUTTONDOWN:

					# Evento de selección de pieza blanca.
					# En este punto no existe ninguna pieza seleccionada.
					if not is_piece_selected:
						piece = select_piece("w")

						# En esta parte se recupera un objeto con todos los movimientos posibles que tiene la ṕieza.
						# Establece el estado como seleccionado.
						if piece is not None:
							possible_moves = piece.get_all_moves(chessboard)
							is_piece_selected = True

					# Evento de selección de pieza por el mouse.
					elif is_piece_selected:
						cell = select_cell()
						special_moves = special_move_gen(chessboard, "w")

						# Verifica si la celda recuperada en el evento de click está dentro de los posibles movimientos
						# para dicha pieza.
						# Es decir, compara la tupla (x, y) del mouse con las tuplas almacenadas.
						if cell in possible_moves:
							prev_x, prev_y = piece.x, piece.y
							prev_pos = [piece.x, piece.y]

							# Posible pieza a ser eliminada.
							kill_piece = chessboard.matrix[cell[0]][cell[1]]

							# Limpieza de sprites obsoletos.
							piece_next_cell = chessboard.move_piece(piece, cell[0], cell[1])
							if piece_next_cell:
								sprite_group.add(piece_next_cell[0])
								sprite_array.append(piece_next_cell[0])
								sprite_group.remove(piece_next_cell[1])
								sprite_array.remove(piece_next_cell[1])

							# Movimientos de rey y torre.
							if type(piece) == King or type(piece) == Rook or type(piece) == Pawn:
								piece.moved = True

							# Remueve de los objetos la pieza eliminada.
							if kill_piece:
								sprite_group.remove(kill_piece)
								sprite_array.remove(kill_piece)

							# Cambio de turno.
							attacked = move_gen(chessboard, "b", True)
							king = chessboard.get_king("w")
							if (king.y, king.x) not in attacked:
								is_piece_selected = False
								player = "AI"
								game_message("Turno actual:\nComputadora", (255, 255, 255))
								moves += 1
								chessboard.save_current_status(moves, piece, prev_pos, False)

								# Si se elimina una pieza, se actualiza el valor para el MinMax.
								if kill_piece:
									chessboard.score -= chessboard.piece_values[type(kill_piece)]

							# Validación para situaciones de jaque del jugador.
							else:
								chessboard.move_piece(piece, prev_y, prev_x)
								if type(piece) == King or type(piece) == Rook:
									piece.moved = False
								chessboard.matrix[cell[0]][cell[1]] = kill_piece
								if kill_piece:
									sprite_group.add(kill_piece)
									sprite_array.append(kill_piece)
								if piece_next_cell:
									sprite_group.add(piece_next_cell[1])
									sprite_array.append(piece_next_cell[1])
								piece.select()

								# Muestra al jugador que se encuentra en jaque..
								if is_in_check:
									game_message('Turno actual:\nJugador, sigue en jaque', (255, 0, 0))
									pygame.display.update()
									pygame.time.wait(1000)
									game_message('Turno actual:\nJugador, en jaque', (255, 0, 0))

								# Movimiento incorrecto.
								else:
									game_message('Turno actual:\nMovimiento suicida', (255, 0, 0))
									pygame.display.update()
									pygame.time.wait(1000)
									game_message('Turno actual:\nJugador', (255, 255, 255))

						# Se encarga de quitar la selección de la casilla actual.
						elif (piece.y, piece.x) == cell:
							piece.not_select()
							is_piece_selected = False

						# Supervición de movimientos especiales.
						elif special_moves and cell in special_moves:
							special = special_moves[cell]
							if (special == "CR" or special == "CL") and type(piece) == King:
								chessboard.move_piece(piece, cell[0], cell[1], special)
								is_piece_selected = False
								player = "AI"
								game_message("Turno actual:\nComputadora", (255, 255, 255))
								moves += 1
								chessboard.save_current_status(moves, piece, prev_pos, False)

							# Movimiento especial inválido.
							else:
								game_message('Turno actual:\nMovimiento inválido', (255, 0, 0))
								pygame.display.update()
								pygame.time.wait(1000)
								if is_in_check:
									game_message('Turno actual:\nJugador', (255, 0, 0))
								else:
									game_message('Turno actual:\nJugador', (255, 255, 255))

						# Movimiento inválido.
						else:
							game_message('Turno actual:\nMovimiento inválido', (255, 0, 0))
							pygame.display.update()
							pygame.time.wait(1000)
							if is_in_check:
								game_message('Turno actual:\nJugador, en jaque', (255, 0, 0))
							else:
								game_message('Turno actual:\nJugador', (255, 255, 255))

					# Eventos de click de botones por el usuario.
					if reset_button.is_cursor_inside(mouse):
						if final_file_name == "":
							reload()
						else:
							load_game(final_file_name)

					#  Botón de carga de documento.
					if load_button.is_cursor_inside(mouse):
						try:
							root = Tk()
							root.iconify()
							root.filename = \
								filedialog.askopenfilename(title="Select file",
															filetypes=(("Plain Text files", "*.txt"), ("all files", "*.*")))
							print(root.filename)
							root.destroy()
							load_game(root.filename)
							final_file_name = root.filename
							ia_mode = "finals"

						except IOError:
							game_message('ERROR\nfile exception', (255, 0, 0))

					if new_button.is_cursor_inside(mouse):
						final_file_name = ""
						reload()

					if ia_mode_button.is_cursor_inside(mouse):
						if ia_mode == "casual":
							ia_mode = "finals"
						else:
							ia_mode = "casual"

		# Botones de funcionalidades.
		if reset_button.is_cursor_inside(cursor=mouse):
			screen.blit(reset_hover, (reset_button.x_offset, reset_button.y_offset))
		else:
			screen.blit(reset, (reset_button.x_offset, reset_button.y_offset))

		if load_button.is_cursor_inside(cursor=mouse):
			screen.blit(load_hover, (load_button.x_offset, load_button.y_offset))
		else:
			screen.blit(load, (load_button.x_offset, load_button.y_offset))

		if new_button.is_cursor_inside(cursor=mouse):
			screen.blit(new_hover, (new_button.x_offset, new_button.y_offset))
		else:
			screen.blit(new, (new_button.x_offset, new_button.y_offset))

		if ia_mode == "casual":
			screen.blit(casual, (ia_mode_button.x_offset, ia_mode_button.y_offset))
		else:
			screen.blit(finals, (ia_mode_button.x_offset, ia_mode_button.y_offset))

		# Actualización de la interface.
		screen.blit(chessboard_background, (0, 0))
		sprite_group.draw(screen)
		pygame.display.update()
		clock.tick(60)


# Guarda el documento en un archivo de log,
def create_log_file(data):
	date_format_string = "%H %M %d-%m-%Y"
	name = "Partida " + datetime.datetime.now().strftime(date_format_string) + '.log'
	file = open(name, "w+")
	file.write(data)
	file.close()


# Función que muestra mensaje de ganador.
def game_over():
	create_log_file(chessboard.get_log_file())
	pygame.display.update()
	pygame.time.wait(2000)
	pygame.event.clear()
	pygame.display.update()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.KEYUP or event.type == pygame.MOUSEBUTTONUP:
				return
			elif event.type == pygame.QUIT:
				import sys
				sys.exit()


if __name__ == "__main__":
	main()
	game_over()
