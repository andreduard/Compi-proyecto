# get the current cell
def get_cell_piece(x, y):
    x = x - 120
    y = y - 60
    return [y // 68, x // 68]


# white pawn moves
def get_white_pawn_moves(cell_value, current_cell, next_cell):
    if current_cell[0] == next_cell[0] + 1 and current_cell[1] == next_cell[1] and cell_value.get_name() == "None":
        return True
    elif cell_value.get_color() == "black" and current_cell[0] == next_cell[0] + 1 and \
            (current_cell[1] + 1 == next_cell[1] or current_cell[1] - 1 == next_cell[1]):
        return True
    else:
        return False


# black pawn moves
def get_black_pawn_moves(cell_value, current_cell, next_cell):
    if current_cell[0] == next_cell[0] - 1 and current_cell[1] == next_cell[1] and cell_value.get_name() == "None":
        return True
    elif cell_value.get_color() == "white" and current_cell[0] == next_cell[0] - 1 and \
            (current_cell[1] + 1 == next_cell[1] or current_cell[1] - 1 == next_cell[1]):
        return True
    else:
        return False


# tower moves
def get_rook_moves(board, cell_value, current_cell, next_cell, current_color):
    current_i = current_cell[0]
    current_j = current_cell[1]

    # vertical move
    if current_cell[0] != next_cell[0] and current_cell[1] == next_cell[1] and \
            cell_value.get_color() != current_color:

        # move to up loop
        if current_cell[0] > next_cell[0]:
            while next_cell[0] < current_cell[0]:
                piece = board[current_cell[0]][next_cell[1]]
                if not piece.get_name() == "None":
                    current_cell[0] = current_i
                    return False
                current_cell[0] -= 1

        # move to down loop
        else:
            while next_cell[0] > current_cell[0]:
                piece = board[current_cell[0]][next_cell[1]]
                if not piece.get_name() == "None":
                    current_cell[0] = current_i
                    return False
                current_cell[0] += 1
        return True

    # horizontal move
    elif current_cell[0] == next_cell[0] and current_cell[1] != next_cell[1] and \
            cell_value.get_color() != current_color:

        # move to right loop
        if current_cell[1] > next_cell[1]:
            while next_cell[1] < current_cell[1]:
                piece = board[next_cell[0]][current_cell[1]]
                if not piece.get_name() == "None":
                    current_cell[1] = current_j
                    return False
                current_cell[1] -= 1

        # move to left loop
        else:
            while next_cell[1] > current_cell[1]:
                piece = board[next_cell[0]][current_cell[1]]
                if not piece.get_name() == "None":
                    current_cell[1] = current_j
                    return False
                current_cell[1] += 1
        return True
    else:
        return False

# knight moves
def get_knight_moves(board, cell_value, current_cell, next_cell, current_color):
    current_i = current_cell[0]
    current_j = current_cell[1]

    # north-west moves

    # 2 steps to left, 1 step up
    if current_cell[1] - 2 == next_cell[1] and current_cell[0] + 1 == next_cell[0] and cell_value.get_color() != current_color:
        piece = board[current_cell[0]][current_cell[1]]
        if not piece.get_name() == "None":
            current_cell[0] = current_i
            current_cell[1] = current_j
            return False
        current_cell[0] += 1
        current_cell[1] -= 2
        return True

    # 2 steps up, 1 step to left
    elif current_cell[1] - 1 == next_cell[1] and current_cell[0] + 2 == next_cell[0] and cell_value.get_color() != current_color:
        piece = board[current_cell[0]][current_cell[1]]
        if not piece.get_name() == "None":
            current_cell[0] = current_i
            current_cell[1] = current_j
            return False
        current_cell[0] += 2
        current_cell[1] -= 1
        return True          

    # north-east moves

    # 2 steps up, 1 step to right
    elif current_cell[1] + 1 == next_cell[1] and current_cell[0] + 2 == next_cell[0] and cell_value.get_color() != current_color:
        piece = board[current_cell[0]][current_cell[1]]
        if not piece.get_name() == "None":
            current_cell[0] = current_i
            current_cell[1] = current_j
            return False
        current_cell[0] += 2
        current_cell[1] += 1
        return True

    # 2 steps to right, 1 step up
    elif current_cell[1] + 2 == next_cell[1] and current_cell[0] + 1 == next_cell[0] and cell_value.get_color() != current_color:
        piece = board[current_cell[0]][current_cell[1]]
        if not piece.get_name() == "None":
            current_cell[0] = current_i
            current_cell[1] = current_j
            return False
        current_cell[0] += 1
        current_cell[1] += 2
        return True

    # south-west moves

    # 2 steps to left, 1 step down
    elif current_cell[1] - 2 == next_cell[1] and current_cell[0] - 1 == next_cell[0] and cell_value.get_color() != current_color:
        piece = board[current_cell[0]][current_cell[1]]
        if not piece.get_name() == "None":
            current_cell[0] = current_i
            current_cell[1] = current_j
            return False
        current_cell[0] -= 1
        current_cell[1] -= 2
        return True

    # 2 steps down, 1 step to left
    elif current_cell[1] - 1 == next_cell[1] and current_cell[0] - 2 == next_cell[0] and cell_value.get_color() != current_color:
        piece = board[current_cell[0]][current_cell[1]]
        if not piece.get_name() == "None":
            current_cell[0] = current_i
            current_cell[1] = current_j
            return False
        current_cell[0] -= 2
        current_cell[1] -= 1
        return True

    # south-east moves

    # 2 steps down, 1 step to right
    elif current_cell[1] + 1 == next_cell[1] and current_cell[0] - 2 == next_cell[0] and cell_value.get_color() != current_color:
        piece = board[current_cell[0]][current_cell[1]]
        if not piece.get_name() == "None":
            current_cell[0] = current_i
            current_cell[1] = current_j
            return False
        current_cell[0] -= 2
        current_cell[1] += 1
        return True

    # 2 steps to right, 1 step down
    elif current_cell[1] + 2 == next_cell[1] and current_cell[0] - 1 == next_cell[0] and cell_value.get_color() != current_color:
        piece = board[current_cell[0]][current_cell[1]]
        if not piece.get_name() == "None":
            current_cell[0] = current_i
            current_cell[1] = current_j
            return False
        current_cell[0] -= 1
        current_cell[1] += 2
        return True

    else:
        return False

# bishop moves
def get_bishop_moves(board, cell_value, current_cell, next_cell, current_color):
    current_i = current_cell[0]
    current_j = current_cell[1]

    # up diagonal move left to right
    if current_cell[0] > next_cell[0] and current_cell[1] < next_cell[1] and cell_value.get_color() != current_color:
        while next_cell[0] < current_cell[0]:
            piece = board[current_cell[0]][current_cell[1]]
            print("pasa por: [" + str(current_cell[0]) + ", " + str(current_cell[1]) + "]")
            if not piece.get_name() == "None":
                current_cell[0] = current_i
                current_cell[1] = current_j
                return False
            current_cell[0] -= 1
            current_cell[1] += 1
        return True

    # down diagonal move right to left
    elif current_cell[0] < next_cell[0] and current_cell[1] > next_cell[1] and cell_value.get_color() != current_color:
        while next_cell[0] > current_cell[0]:
            piece = board[current_cell[0]][current_cell[1]]
            if not piece.get_name() == "None":
                current_cell[0] = current_i
                current_cell[1] = current_j
                return False
            current_cell[0] += 1
            current_cell[1] -= 1
        return True

    # up diagonal move right to left
    elif current_cell[0] > next_cell[0] and current_cell[1] > next_cell[1] and cell_value.get_color() != current_color:
        while next_cell[0] > current_cell[0]:
            piece = board[current_cell[0]][current_cell[1]]
            if not piece.get_name() == "None":
                current_cell[0] = current_i
                current_cell[1] = current_j
                return False
            current_cell[0] -= 1
            current_cell[1] -= 1
        return True

    # down diagonal move left to right
    elif current_cell[0] < next_cell[0] and current_cell[1] < next_cell[1] and cell_value.get_color() != current_color:
        while next_cell[0] < current_cell[0]:
            piece = board[current_cell[0]][current_cell[1]]
            if not piece.get_name() == "None":
                current_cell[0] = current_i
                current_cell[1] = current_j
                return False
            current_cell[0] += 1
            current_cell[1] += 1
        return True
    else:
        return False


# queen moves
def get_queen_moves(board, cell_value, current_cell, next_cell, current_color):
    return get_rook_moves(board, cell_value, current_cell, next_cell, current_color) or \
           get_bishop_moves(board, cell_value, current_cell, next_cell, current_color)


# king moves
def get_king_moves(cell_value, current_cell, next_cell, current_color):
    print("posición actual: [" + str(current_cell[0]) + ", " + str(current_cell[1]) + "]")
    print("posición siguiente: [" + str(next_cell[0]) + ", " + str(next_cell[1]) + "]")
    if cell_value.get_color() != current_color:

        # vertical move
        if current_cell[1] == next_cell[1] and (current_cell[0] + 1 == next_cell[0] or
                                                current_cell[0] - 1 == next_cell[0]):
            return True

        # horizontal move
        elif current_cell[0] == next_cell[0] and (current_cell[1] - 1 == next_cell[1] or
                                                  current_cell[1] + 1 == next_cell[1]):
            return True

        # up diagonal moves
        elif current_cell[0] - 1 == next_cell[0] and (current_cell[1] - 1 == next_cell[1]
                                                      or current_cell[1] + 1 == next_cell[1]):
            return True

        # down diagonal moves
        elif current_cell[0] + 1 == next_cell[0] and (current_cell[1] - 1 == next_cell[1]
                                                      or current_cell[1] + 1 == next_cell[1]):
            return True
        else:
            return False
    else:
        return False
