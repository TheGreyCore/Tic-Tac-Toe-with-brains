from src.board import Board
from src.brain import Enemy

board = Board()
enemy = Enemy()

board.print_board()
while not board.is_game_over():

    # Player turn
    move = input("Make your move: ")
    move.split(" ")
    print("""
    
    """)
    print("Player move")
    board.make_move(int(move[0]), int(move[2]))

    if board.is_game_over():
        board.print_board()
        break

    # Enemy turn
    print("Enemy move")
    board.make_move(*enemy.make_move(board))

    board.print_board()
