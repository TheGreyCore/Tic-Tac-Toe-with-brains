from src.board import Board

board = Board()


# board.print_board()
board.make_move(0, 0)
# board.print_board()
board.make_move(0, 2)
# board.print_board()
board.make_move(1, 1)
board.make_move(1, 2)
board.make_move(2, 2)
print(board.is_game_over())
board.print_board()
# print(board.get_all_available_moves())
