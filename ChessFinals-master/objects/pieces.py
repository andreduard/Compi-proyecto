import pygame

"""
------------------------------------------------------------------------------------------------------------------------
---------- CLASE PIEZA -------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
"""


# Clase que permite el manejo de las Piezas del tablero.
# Esta clase está implementada como objeto madre para las demás piezas (herencia).
class Piece(pygame.sprite.Sprite):

	def __init__(self, color, y, x):
		super().__init__()  # Sprite.

		# Atributos de la clase pieza.
		self.sprite = None
		self.color = color
		self.x, self.y = x, y

		# Inicialización de aspectos gráficos de la casilla.
		# Permite la carga de la imagen y la inicialización de la casilla parael marcado y selección.
		self.image = pygame.Surface((70, 70), pygame.SRCALPHA, 32)
		self.image.convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.x, self.rect.y = x * 70, y * 70
		self.is_select = False
		self.is_focused = False

	# Función que retorna una lista de movimientos válidos en formato tupla (coordenadas) para las piezas que pueden
	# moverse vertical y horizontalmente.
	def get_all_vertical_horizontal_moves(self, chessboard):
		moves = set()

		# Movimientos horizontales posibles.
		next_y = self.y
		for i in (-1, 1):
			next_x = self.x
			while 1:
				next_x += i
				if move_piece(self.color, next_y, next_x, chessboard):
					moves.add((next_y, next_x))
					if kill_piece(self.color, next_y, next_x, chessboard):
						break
				else:
					break

		# Movimientos verticales posibles.
		next_x = self.x
		for i in (-1, 1):
			next_y = self.y
			while 1:
				next_y += i
				if move_piece(self.color, next_y, next_x, chessboard):
					moves.add((next_y, next_x))
					if kill_piece(self.color, next_y, next_x, chessboard):
						break
				else:
					break
		return moves

	# Función que retorna una lista de movimientos válidos en formato tupla (coordenadas) para las piezas que pueden
	# moverse diagonalmente.
	def get_all_diagonal_moves(self, chessboard):
		moves = set()
		sums = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
		for s in sums:
			next_x = self.x
			next_y = self.y
			while 1:
				next_x += s[0]
				next_y += s[1]
				if move_piece(self.color, next_y, next_x, chessboard):
					moves.add((next_y, next_x))
					if kill_piece(self.color, next_y, next_x, chessboard):
						break
				else:
					break
		return moves

	# Función que muestra una casilla como marcada.
	def select(self):
		pygame.draw.rect(self.image, (128, 128, 128), (0, 0, 70, 70), 5)
		self.is_select = True

	# Función que quita la marca de una casilla.
	def not_select(self):
		self.image = pygame.Surface((70, 70), pygame.SRCALPHA, 32)
		self.image.convert_alpha()
		self.image.blit(self.sprite, (0, 0))
		self.is_select = False

	def focus_moved(self):
		pygame.draw.rect(self.image, (255, 128, 128), (0, 0, 70, 70), 5)
		self.is_focused = True

	def un_focus_moved(self):
		self.image = pygame.Surface((70, 70), pygame.SRCALPHA, 32)
		self.image.convert_alpha()
		self.image.blit(self.sprite, (0, 0))
		self.is_focused = False

	# Funciones GET/SET
	def get_color(self):
		return self.color

	def get_x(self):
		return self.x

	def get_y(self):
		return self.y

	def set_color(self, color):
		self.color = color

	def set_x(self, x):
		self.x = x

	def set_y(self, y):
		self.y = y


"""
------------------------------------------------------------------------------------------------------------------------
---------- CLASES POR TIPO DE PIEZA (HERENCIA) -------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
"""


class Pawn(Piece):

	def __init__(self, color, y, x):
		super().__init__(color, y, x)  # Pieza.
		self.symbol = "P"
		self.moved = False

		# Verificación de color para la inicialización de la pieza en la interfaz.
		if self.color == "b":
			self.sprite = pygame.image.load("resources/pieces/black-pawn.png".format(self.color))
		else:
			self.sprite = pygame.image.load("resources/pieces/white-pawn.png".format(self.color))
		self.image.blit(self.sprite, (0, 0))

	# Movimientos esperados para el tipo de pieza Peón.
	def get_all_moves(self, chessboard):
		move_set = set()

		next_y = self.y - 1 if self.color == "w" else self.y + 1
		if 0 <= next_y < 8 and chessboard.matrix[next_y][self.x] is None:
			move_set.add((next_y, self.x))

		# Si el peón no se ha movido, generar las siguientes dos, verificar que no hayan piezas en el destino
		if not self.moved:
			if self.color == "w":
				if chessboard.matrix[self.y - 2][self.x] is None:
					move_set.add((self.y - 2, self.x))
			elif self.color == "b":
				if chessboard.matrix[self.y + 2][self.x] is None:
					move_set.add((self.y + 2, self.x))

		# Agregar aquellas casillas que esté atacando
		attack_set = self.get_attacked(chessboard)
		move_set.update(attack_set)

		return move_set

	def get_attacked(self, chessboard):
		"""
		Retorna todas las casillas que ataca este peón
		"""
		move_set = set()
		sums = [-1, 1]

		for s in sums:
			next_x = self.x + s
			next_y = self.y - 1 if self.color == "w" else self.y + 1
			if move_piece(self.color, next_y, next_x, chessboard) and kill_piece(self.color, next_y, next_x, chessboard):
				move_set.add((next_y, next_x))
			else:
				continue
		return move_set


class Rook(Piece):

	def __init__(self, color, y, x):
		super().__init__(color, y, x)
		self.symbol = "T"

		# Verificación de color para la inicialización de la pieza en la interfaz.
		if self.color == "b":
			self.sprite = pygame.image.load("resources/pieces/black-rook.png".format(self.color))
		else:
			self.sprite = pygame.image.load("resources/pieces/white-rook.png".format(self.color))
		self.image.blit(self.sprite, (0, 0))
		self.moved = False

	def get_all_moves(self, chessboard):
		return self.get_all_vertical_horizontal_moves(chessboard)


class Bishop(Piece):

	def __init__(self, color, y, x):
		super().__init__(color, y, x)
		self.symbol = "A"

		# Verificación de color para la inicialización de la pieza en la interfaz.
		if self.color == "b":
			self.sprite = pygame.image.load("resources/pieces/black-bishop.png".format(self.color))
		else:
			self.sprite = pygame.image.load("resources/pieces/white-bishop.png".format(self.color))
		self.image.blit(self.sprite, (0, 0))

	def get_all_moves(self, chessboard):
		return self.get_all_diagonal_moves(chessboard)


class Knight(Piece):

	def __init__(self, color, y, x):
		super().__init__(color, y, x)
		self.symbol = "C"

		# Verificación de color para la inicialización de la pieza en la interfaz.
		if self.color == "b":
			self.sprite = pygame.image.load("resources/pieces/black-knight.png".format(self.color))
		else:
			self.sprite = pygame.image.load("resources/pieces/white-knight.png".format(self.color))
		self.image.blit(self.sprite, (0, 0))

	def get_all_moves(self, chessboard):
		moves = set()
		sums = [(2, 1), (1, 2), (2, -1), (-1, 2), (-2, 1), (1, -2), (-2, -1), (-1, -2)]
		for s in sums:
			next_x = self.x + s[0]
			next_y = self.y + s[1]
			if move_piece(self.color, next_y, next_x, chessboard):
				moves.add((next_y, next_x))
		return moves


class King(Piece):

	def __init__(self, color, y, x):
		super().__init__(color, y, x)
		self.symbol = "R"

		# Verificación de color para la inicialización de la pieza en la interfaz.
		if self.color == "b":
			self.sprite = pygame.image.load("resources/pieces/black-king.png".format(self.color))
		else:
			self.sprite = pygame.image.load("resources/pieces/white-king.png".format(self.color))
		self.image.blit(self.sprite, (0, 0))
		self.moved = False

	def get_all_moves(self, chessboard):
		moves = set()
		sums = [(1, 1), (1, 0), (0, 1), (1, -1), (-1, 1), (-1, 0), (0, -1), (-1, -1)]
		for s in sums:
			next_x = self.x + s[0]
			next_y = self.y + s[1]
			if move_piece(self.color, next_y, next_x, chessboard):
				moves.add((next_y, next_x))
		return moves


class Queen(Piece):

	def __init__(self, color, y, x):
		super().__init__(color, y, x)
		self.symbol = "Q"

		# Verificación de color para la inicialización de la pieza en la interfaz.
		if self.color == "b":
			self.sprite = pygame.image.load("resources/pieces/black-queen.png".format(self.color))
		else:
			self.sprite = pygame.image.load("resources/pieces/white-queen.png".format(self.color))
		self.image.blit(self.sprite, (0, 0))

	def get_all_moves(self, chessboard):
		get_all_vertical_horizontal_moves = self.get_all_vertical_horizontal_moves(chessboard)
		diagonal_moves = self.get_all_diagonal_moves(chessboard)
		return get_all_vertical_horizontal_moves.union(diagonal_moves)


"""
------------------------------------------------------------------------------------------------------------------------
---------- FUNCIONES AUXILIARES ----------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
"""


# Se encarga de la acción de comer una pieza del tablero.
def kill_piece(color, y, x, chessboard):
	piece = chessboard.matrix[y][x]
	if piece is None:
		return False
	else:
		return True if piece.color != color else False


# Se encarga de validar el movimiento por coordenada y color.
def move_piece(color, y, x, chessboard):
	if x < 0 or x > 7 or y < 0 or y > 7:
		return False
	piece = chessboard.matrix[y][x]
	if piece is None:
		return True
	else:
		return True if piece.color != color else False
