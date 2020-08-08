from objects.pieces import *


def matrix_to_tuple(array, empty_array):
    """
    Given a 2D list, converts it to 2D tuple. This is useful for using a
    matrix as a key in a dictionary
    (an empty 8x8 should be provided, just for efficiency)
    """
    for i in range(8):
        empty_array[i] = tuple(array[i])
    return tuple(empty_array)


def check_castling(chessboard, c, side):
    """
    Checks if castling is possible, given a chessboard state, a color, and the side
    for the castle.
    """
    castle_left = False
    castle_right = False

    if c == "w":
        king = chessboard.white_king
        left_rook = chessboard.white_rook_left
        right_rook = chessboard.white_rook_right
        attacked = move_gen(chessboard, "b", True)
        row = 7
    elif c == "b":
        king = chessboard.black_king
        left_rook = chessboard.black_rook_left
        right_rook = chessboard.black_rook_right
        attacked = move_gen(chessboard, "w", True)
        row = 0
    else:
        raise ValueError

    if not king.moved:  # cannot castle if the king has moved
        # left castle, check to see if the rook has moved
        if chessboard.matrix[row][0] == left_rook and not left_rook.moved:
            # squares between the rook and the king have to be empty and cannot be in check
            squares = {(row, 1), (row, 2), (row, 3)}
            if not chessboard.matrix[row][1] and not chessboard.matrix[row][2] and not chessboard.matrix[row][3]:
                if not attacked.intersection(squares):
                    castle_left = True
        # right castle
        if chessboard.matrix[row][7] == right_rook and not right_rook.moved:
            # squares between the rook and the king have to be empty and cannot be in check
            squares = {(row, 6), (row, 5)}
            if not chessboard.matrix[row][6] and not chessboard.matrix[row][5]:
                if not attacked.intersection(squares):
                    castle_right = True

    if side == "r":
        return castle_right
    elif side == "l":
        return castle_left


def special_move_gen(chessboard, color, moves=None):
    """
    From a chessboard state and a color, returns a move dict with the possible
    special moves. Currently only returns castling moves as pawn promotion is
    implemented in a different way.

    Key in the moves dict is where the player has to 'click' to perform the move.
    Value is the special move code.
    """
    if moves is None:
        moves = dict()
    if color == "w":
        x = 7
    elif color == "b":
        x = 0
    else:
        raise ValueError
    right_castle = check_castling(chessboard, color, "r")
    left_castle = check_castling(chessboard, color, "l")

    if right_castle:
        moves[(x, 6)] = "CR"
    if left_castle:
        moves[(x, 2)] = "CL"

    return moves


def move_gen(chessboard, color, attack=False):
    """
    Generates the pseudo-legal moves from a chessboard state, for a specific color.
    Does not check to see if the move puts you in check, this must be done
    outside of the function.
    Returns:
    attc = False: moves (dict) - maps coord (y,x) to a set containing the coords of
                                where it can legally move
    attc = True: moves (set) - the set of attacked squares for that color.
    """
    if attack:
        moves = set()
    else:
        moves = dict()

    # Generates all the legal moves for all the pieces, then combines them
    for j in range(8):
        for i in range(8):
            piece = chessboard.matrix[i][j]
            if piece is not None and piece.color == color:
                legal_moves = piece.get_all_moves(chessboard)
                if legal_moves and not attack:
                    moves[(i, j)] = legal_moves
                elif legal_moves and attack:
                    moves = moves.union(legal_moves)

    return moves


# IF FUNCTION RETURNS value= -INF (or move = 0), AI IS IN CHECKMATE
# (returning +inf for value indicates player checkmate)
# noinspection PyBroadException
def minimax(chessboard, depth, alpha, beta, maximizing, memo, finals):
    """
    Minimax algorithm with alpha-beta pruning determines the best move for
    black from the current chessboard state.
    Returns: bestValue - score of the chessboard resulting from the best move
            move - tuple containing the start coord and the end coord of the best move
            ex. ((y1,x1),(y2,x2)) -> the piece at (y1,x1) should move to (y2,x2)

    Note: 0 is used as a placeholder when returning from the function, when we
    don't care about the move (eg. the algorithm is exploring options, don't
    need to return a 'move')
    """

    # convert the 2D list to a tuple, so it can be used as a key in memo
    tuple_mat = matrix_to_tuple(chessboard.matrix, chessboard.get_null_row())

    if finals:
        initial_depth = 8
    else:
        initial_depth = 4

    if tuple_mat in memo and depth != initial_depth:  # set this to the depth of the initial call
        return memo[tuple_mat], 0

    if depth == 0:  # end of the search is reached
        memo[tuple_mat] = chessboard.score
        return chessboard.score, 0

    if maximizing:
        best_value = float("-inf")
        black_moves = move_gen(chessboard, "b")

        # explore all the potential moves from this chessboard state
        for start, move_set in black_moves.items():
            for end in move_set:

                # First I'll preserve the score
                previous_score = chessboard.score

                # perform the move
                # preserve the start and the end pieces, in case the move
                # needs to be reversed
                piece = chessboard.matrix[start[0]][start[1]]
                dest = chessboard.matrix[end[0]][end[1]]

                # if a pawn promotion occurs, return the pieces involved
                pawn_promotion = chessboard.move_piece(piece, end[0], end[1])

                moved_piece = False
                if isinstance(piece, Pawn) or isinstance(piece, Rook) or isinstance(piece, King):
                    moved_piece = piece.moved
                    piece.moved = True

                # see if the move puts you in check
                attacked = move_gen(chessboard, "w", True)  # return spaces attacked by white
                king = chessboard.get_king("b")
                if (king.y, king.x) in attacked:
                    # reverse the move
                    chessboard.move_piece(piece, start[0], start[1], True)
                    chessboard.matrix[end[0]][end[1]] = dest
                    if pawn_promotion:
                        chessboard.score -= 9  # revert the score from the promotion
                    continue  # the move is illegal, thus we don't care and move on

                # If this moves places the piece in a bad position, this board is worse
                # // 2 so that it might choose to sacrifice the piece
                if (piece.y, piece.x) in attacked:
                    chessboard.score -= chessboard.piece_values[type(piece)] // 2

                # change the score if a piece was captured
                if dest is not None:
                    chessboard.score += chessboard.piece_values[type(dest)]

                # now I'll check the attacked locations for this player, the more attacked the better
                attacked_slots = move_gen(chessboard, "b", True)
                chessboard.score += len(attacked_slots)

                # search deeper for the children, this time its the minimizing
                # player's turn
                v, __ = minimax(chessboard, depth - 1, alpha, beta, False, memo, finals)

                # revert the chessboard and the score
                chessboard.move_piece(piece, start[0], start[1], True)
                chessboard.matrix[end[0]][end[1]] = dest
                if isinstance(piece, Pawn) or isinstance(piece, Rook) or isinstance(piece, King):
                    piece.moved = moved_piece

                chessboard.score = previous_score

                if v >= best_value:  # move is better than best, store it
                    move = (start, (end[0], end[1]))

                best_value = max(best_value, v)
                alpha = max(alpha, best_value)

                if beta <= alpha:
                    return best_value, move
        try:
            return best_value, move

        except:
            return best_value, 0  # no best move was found, indicates AI in checkmate

    else:  # (* minimizing player *)
        best_value = float("inf")
        white_moves = move_gen(chessboard, "w")

        # explore all the potential moves from this chessboard state
        for start, move_set in white_moves.items():
            for end in move_set:

                # First I'll preserve the score
                previous_score = chessboard.score

                # perform the move
                piece = chessboard.matrix[start[0]][start[1]]
                dest = chessboard.matrix[end[0]][end[1]]
                pawn_promotion = chessboard.move_piece(piece, end[0], end[1])

                moved_piece = False
                if isinstance(piece, Pawn) or isinstance(piece, Rook) or isinstance(piece, King):
                    moved_piece = piece.moved
                    piece.moved = True

                # see if the move puts you in check
                attacked = move_gen(chessboard, "b", True)  # return spaces attacked by black
                king = chessboard.get_king("w")
                if (king.y, king.x) in attacked:
                    # reverse the move
                    chessboard.move_piece(piece, start[0], start[1], True)
                    chessboard.matrix[end[0]][end[1]] = dest
                    if pawn_promotion:
                        chessboard.score -= 9  # revert the score from the promotion
                    continue  # the move is illegal, thus we don't care and move on

                # If this moves places the piece in a bad position, this board is worse
                # // 2 so that it might choose to sacrifice the piece
                if (piece.y, piece.x) in attacked:
                    chessboard.score += chessboard.piece_values[type(piece)] // 2

                # update the score
                if dest is not None:
                    chessboard.score -= chessboard.piece_values[type(dest)]

                # now I'll check the attacked locations for this player, the more attacked the better
                attacked_slots = move_gen(chessboard, "w", True)
                chessboard.score -= len(attacked_slots)

                v, __ = minimax(chessboard, depth - 1, alpha, beta, True, memo, finals)

                best_value = min(v, best_value)
                beta = min(beta, best_value)

                # reverse the move, revert the score
                chessboard.move_piece(piece, start[0], start[1], True)
                chessboard.matrix[end[0]][end[1]] = dest
                if isinstance(piece, Pawn) or isinstance(piece, Rook) or isinstance(piece, King):
                    piece.moved = moved_piece

                chessboard.score = previous_score

                if pawn_promotion:
                    chessboard.score += 9
                if dest is not None:
                    chessboard.score += chessboard.piece_values[type(dest)]

                if beta <= alpha:
                    return best_value, 0

        return best_value, 0
