from random import choice
from copy import deepcopy


class Enemy:
    def __int__(self):
        pass

    def make_move(self, board):
        available_moves = board.get_all_available_moves()

        # Make a copy of the existing board and check all possible next moves for a win.
        for i in range(len(available_moves)):
            possible_row = available_moves[i][0]
            possible_column = available_moves[i][0]
            copy_board = deepcopy(board)

            if copy_board.is_space_empty(possible_row, possible_column):
                copy_board.make_move(possible_row, possible_column)

                # check is game over after move or not
                if copy_board.is_game_over():
                    return possible_row, possible_column
                else:
                    return choice(available_moves)
