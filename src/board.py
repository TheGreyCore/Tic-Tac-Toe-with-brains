class Board:
    def __init__(self):
        self.board = []
        for _ in range(0, 3):
            self.board.append([".", ".", "."])
        self.x_turn = True
        self.moves = 0

    def print_board(self):
        print(self.board[0])
        print(self.board[1])
        print(self.board[2])

    def make_move(self, row, column):
        if self.is_space_empty(row, column):
            if self.x_turn:
                self.board[row][column] = "X"
            else:
                self.board[row][column] = "0"
            self.x_turn = not self.x_turn
            self.moves += 1
        else:
            raise Exception("You are attempting to move on occupied space")

    def is_space_empty(self, row, column):
        if self.board[row][column] == ".":
            return True
        else:
            return False

    def get_all_available_moves(self):
        available_moves = []
        for row in range(0, 3):
            for column in range(0, 3):
                if self.is_space_empty(row, column):
                    available_moves.append([row, column])
        return available_moves

    def is_game_over(self):

        # Game is winnable if at least 5 moves are done
        if self.moves < 5:
            return False

        # Check rows for win
        for row in range(3):
            unique_rows = set(self.board[row])
            if len(unique_rows) == 1:
                value = unique_rows.pop()
                if value is not None:
                    return value

        # Check columns for win
        for col in range(3):
            unique_columns = set()
            for row in range(3):
                unique_columns.add(self.board[row][col])

            if len(unique_columns) == 1:
                value = unique_columns.pop()
                if value is not None:
                    return value

        # Check backwards diagonal for win
        backwards_diagonal = set()
        backwards_diagonal.add(self.board[0][0])
        backwards_diagonal.add(self.board[1][1])
        backwards_diagonal.add(self.board[2][2])

        if len(backwards_diagonal) == 1:
            value = backwards_diagonal.pop()
            if value is not None:
                return value

        # Check forwards diagonal for win
        forwards_diagonal = set()
        forwards_diagonal.add(self.board[2][0])
        forwards_diagonal.add(self.board[1][1])
        forwards_diagonal.add(self.board[0][2])

        if len(forwards_diagonal) == 1:
            value = forwards_diagonal.pop()
            if value is not None:
                return value

        # If there is no winner return None
        return None
