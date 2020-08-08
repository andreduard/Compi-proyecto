from objects.pieces import *


def location_translator(row, column):
	if column == 'a':
		return 8 - row, 0
	elif column == 'b':
		return 8 - row, 1
	elif column == 'c':
		return 8 - row, 2
	elif column == 'd':
		return 8 - row, 3
	elif column == 'e':
		return 8 - row, 4
	elif column == 'f':
		return 8 - row, 5
	elif column == 'g':
		return 8 - row, 6
	elif column == 'h':
		return 8 - row, 7


def str_local_translator(row, column):
	if row == 0:
		return "A" + str(8 - column)
	elif row == 1:
		return "B" + str(8 - column)
	elif row == 2:
		return "C" + str(8 - column)
	elif row == 3:
		return "D" + str(8 - column)
	elif row == 4:
		return "E" + str(8 - column)
	elif row == 5:
		return "F" + str(8 - column)
	elif row == 6:
		return "G" + str(8 - column)
	else:
		return "H" + str(8 - column)


"""
------------------------------------------------------------------------------------------------------------------------
---------- CLASE TABLERO -----------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
"""


class Chessboard:

	def __init__(self, filename=None):

		# Valores iniciales para el algoritmo de MinMax
		self.score = 0
		self.piece_values = {King: 200, Queen: 10, Rook: 5, Knight: 3, Bishop: 3, Pawn: 1}
		self.log = ""

		# Piezas negras.
		self.black_rook_left = Rook("b", 0, 0)
		self.black_knight_left = Knight("b", 0, 1)
		self.black_bishop_left = Bishop("b", 0, 2)
		self.black_queen = Queen("b", 0, 3)
		self.black_king = King("b", 0, 4)
		self.black_bishop_right = Bishop("b", 0, 5)
		self.black_knight_right = Knight("b", 0, 6)
		self.black_rook_right = Rook("b", 0, 7)

		# Piezas blancas.
		self.white_rook_left = Rook("w", 7, 0)
		self.white_knight_left = Knight("w", 7, 1)
		self.white_bishop_left = Bishop("w", 7, 2)
		self.white_queen = Queen("w", 7, 3)
		self.white_king = King("w", 7, 4)
		self.white_bishop_right = Bishop("w", 7, 5)
		self.white_knight_right = Knight("w", 7, 6)
		self.white_rook_right = Rook("w", 7, 7)

		# Tablero logico del juego.
		# Valida si la carga es de un tablero prestablecido o si es tablero completo,
		if filename is None:
			self.matrix = [
				[self.black_rook_left, self.black_knight_left, self.black_bishop_left, self.black_queen,
				 self.black_king, self.black_bishop_right, self.black_knight_right, self.black_rook_right],
				self.get_pawn_row("b"),
				self.get_null_row(), self.get_null_row(), self.get_null_row(), self.get_null_row(),
				self.get_pawn_row("w"),
				[self.white_rook_left, self.white_knight_left, self.white_bishop_left, self.white_queen,
				 self.white_king, self.white_bishop_right, self.white_knight_right, self.white_rook_right]
			]
		else:
			self.matrix = [
				[None, None, None, None, None, None, None, None],
				[None, None, None, None, None, None, None, None],
				[None, None, None, None, None, None, None, None],
				[None, None, None, None, None, None, None, None],
				[None, None, None, None, None, None, None, None],
				[None, None, None, None, None, None, None, None],
				[None, None, None, None, None, None, None, None],
				[None, None, None, None, None, None, None, None]
			]
			file = open(filename, 'r')
			line = file.readline()
			while line != "":
				x, y = location_translator(int(line[3]), line[2])
				print("Pieza: " + line[0] + line[1] + ", coordenadas: (" + str(x) + ", " + str(y) + ")")
				if line[0] == 'B':
					if line[1] == 'R':
						self.matrix[x][y] = King("b", x, y)
					elif line[1] == 'D':
						self.matrix[x][y] = Queen("b", x, y)
					elif line[1] == 'T':
						self.matrix[x][y] = Rook("b", x, y)
					elif line[1] == 'A':
						self.matrix[x][y] = Bishop("b", x, y)
					elif line[1] == 'C':
						self.matrix[x][y] = Knight("b", x, y)
					elif line[1] == 'P':
						self.matrix[x][y] = Pawn("b", x, y)
				else:
					if line[1] == 'R':
						self.matrix[x][y] = King("w", x, y)
					elif line[1] == 'D':
						self.matrix[x][y] = Queen("w", x, y)
					elif line[1] == 'T':
						self.matrix[x][y] = Rook("w", x, y)
					elif line[1] == 'A':
						self.matrix[x][y] = Bishop("w", x, y)
					elif line[1] == 'C':
						self.matrix[x][y] = Knight("w", x, y)
					elif line[1] == 'P':
						self.matrix[x][y] = Pawn("w", x, y)
				# self.save_current_status(0)
				line = file.readline()
			file.close()

			# Se establece que todas las piezas han sido movidas al menos una vez
			for row in self.matrix:
				for piece in row:
					if isinstance(piece, Pawn) or isinstance(piece, King) or isinstance(piece, Rook):
						piece.moved = True

	# Función que retorna una fila de peones para la matriz de juego.
	@staticmethod
	def get_pawn_row(color):
		return [Pawn("w", 6, i) for i in range(8)] if color == "w" else [Pawn("b", 1, i) for i in range(8)]

	# Función que devuelve una fila vacía.
	# noinspection PyUnusedLocal
	@staticmethod
	def get_null_row():
		return [None for i in range(8)]

	# Función que devuelve una fila de coordenadas vacías.
	# noinspection PyUnusedLocal
	@staticmethod
	def get_empty_row_column():
		return [[None for x in range(8)] for y in range(8)]

	# Valida la promoción de un peón.
	@staticmethod
	def is_promotion(piece, y):
		if piece.color == "w":
			row, inc = 1, -1
		else:
			row, inc = 6, 1
		return True if type(piece) == Pawn and piece.y == row and y == piece.y + inc else False

	# Recupera el log
	def get_log_file(self):
		return self.log

	# Función que se encarga de setear el movimiento de la pieza por el tablero.
	def move_piece(self, piece, y, x, np=False):
		promotion = self.is_promotion(piece, y)
		prev_x, prev_y = piece.x, piece.y
		piece.x, piece.y = x, y
		piece.rect.x, piece.rect.y = x * 70, y * 70
		self.matrix[prev_y][prev_x] = None

		# Aquí se gana una pieza por la promoción de un peón.
		# Por defecto es una reina.
		# Se modifica el score para el min max ya que se perdió un peon pero se ganó una reina.
		if promotion and not np:
			self.matrix[y][x] = Queen(piece.color, y, x)
			if piece.color == "w":
				self.score -= 9
			elif piece.color == "b":
				self.score += 9
			return self.matrix[y][x], piece
		else:
			self.matrix[y][x] = piece
			piece.not_select()
			if np == "CR":
				# Enroque derecho:		corto
				self.matrix[y][x-1] = self.matrix[y][x+1]
				self.matrix[y][x+1] = None
			elif np == "CL":
				# Enroque izquierdo:	largo
				self.matrix[y][x + 1] = self.matrix[y][0]
				self.matrix[y][0] = None

	# Recupera la pieza Rey.
	def get_king(self, color):
		if color == "b":
			for row in self.matrix:
				for piece in row:
					if isinstance(piece, King) and piece.color == "b":
						return piece
		else:
			for row in self.matrix:
				for piece in row:
					if isinstance(piece, King) and piece.color == "w":
						return piece
		raise ValueError('King not found')

	# Imprime el tablero.
	def save_current_status(self, moves, piece, cell, isIa):
		chars = ["A", "B", "C", "D", "E", "F", "G", "H"]
		numbers = ["8", "7", "6", "5", "4", "3", "2", "1"]

		# Se valida el tipo de jugador, ya que IA tiene invertidos el (x, y).
		if isIa:
			prev_pos = str_local_translator(cell[1], cell[0])
		else:
			prev_pos = str_local_translator(cell[0], cell[1])

		# Recuperación de movimientos totales.
		current_status = "Movimientos totales: " + str(moves) + "\n\n"
		if moves % 2 == 0:
			current_status += "Turno de IA.\n\n"
		else:
			current_status += "Turno de humano.\n\n"

		# Se agrega el dato de movimiento.
		current_status += "Movimiento registrado:\n" + piece.color + piece.symbol + "-" + prev_pos + " => " + \
							piece.color + piece.symbol + "-" + str_local_translator(piece.x, piece.y) + "\n"

		# Ciclo de almacenamiento de tablero.
		for i in range(9):
			if i < 8:
				for j in range(9):
					if j < 8:
						piece = self.matrix[i][j]
						if piece is not None:
							current_status += "\t" + piece.color + piece.symbol + "\t"
						else:
							current_status += "\t\t"
					else:
						current_status += "\t" + numbers[i] + "\n\n"
			else:
				current_status += "\n"
				for char in chars:
					current_status += "\t" + char + "\t"
		self.log += current_status + "\n\n\n\n"
