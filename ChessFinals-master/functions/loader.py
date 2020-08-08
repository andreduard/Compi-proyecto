from objects.piece import *


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


def load_file(filename):

	none_piece = Piece("None", "None")
	board = [
		[none_piece, none_piece, none_piece, none_piece, none_piece, none_piece, none_piece, none_piece],
		[none_piece, none_piece, none_piece, none_piece, none_piece, none_piece, none_piece, none_piece],
		[none_piece, none_piece, none_piece, none_piece, none_piece, none_piece, none_piece, none_piece],
		[none_piece, none_piece, none_piece, none_piece, none_piece, none_piece, none_piece, none_piece],
		[none_piece, none_piece, none_piece, none_piece, none_piece, none_piece, none_piece, none_piece],
		[none_piece, none_piece, none_piece, none_piece, none_piece, none_piece, none_piece, none_piece],
		[none_piece, none_piece, none_piece, none_piece, none_piece, none_piece, none_piece, none_piece],
		[none_piece, none_piece, none_piece, none_piece, none_piece, none_piece, none_piece, none_piece],
	]
	if filename == "":
		return "", None
	file = open(filename, 'r')
	line = file.readline()

	while line != "":
		x, y = location_translator(int(line[3]), line[2])
		if line[0] == 'B':
			if line[1] == 'R':
				board[x][y] = Piece("black", 'king')
			elif line[1] == 'D':
				board[x][y] = Piece("black", 'queen')
			elif line[1] == 'T':
				board[x][y] = Piece("black", 'rook')
			elif line[1] == 'A':
				board[x][y] = Piece("black", 'bishop')
			elif line[1] == 'C':
				board[x][y] = Piece("black", 'knight')
			elif line[1] == 'P':
				board[x][y] = Piece("black", 'pawn')
		else:
			if line[1] == 'R':
				board[x][y] = Piece("white", 'king')
			elif line[1] == 'D':
				board[x][y] = Piece("white", 'queen')
			elif line[1] == 'T':
				board[x][y] = Piece("white", 'rook')
			elif line[1] == 'A':
				board[x][y] = Piece("white", 'bishop')
			elif line[1] == 'C':
				board[x][y] = Piece("white", 'knight')
			elif line[1] == 'P':
				board[x][y] = Piece("white", 'pawn')
		line = file.readline()
	file.close()

	return filename, board
