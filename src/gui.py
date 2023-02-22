from tkinter import Tk, Button, PhotoImage
from tkinter import messagebox
from src.board import Board
from src.brain import Enemy


board = Board()
enemy = Enemy()

# Color scheme
BACKGROUND = "#658864"


def create_board_buttons(root):
    empty_field = PhotoImage(file="src/images/empty_field.png")
    board_buttons = []
    for column_id in range(0, 3):
        row = []
        for row_id in range(0, 3):
            row.append(Button(
                root,
                image=empty_field,
                highlightthickness=0,
                bd=0,
                activebackground=BACKGROUND,
            ))
            row[row_id].grid(row=row_id, column=column_id)
        board_buttons.append(row)
    return board_buttons


class GUI:
    def __init__(self):
        # Window settings
        self.root = Tk()
        self.root.title("Tic Tac Toe!")
        self.root.config(padx=10, pady=10, background=BACKGROUND)

        # Create buttons
        empty_field = PhotoImage(file="src/images/empty_field.png")
        self.board_buttons = []
        for row_id in range(0, 3):
            for column_id in range(0, 3):
                self.board_buttons.append(Button(
                    self.root,
                    image=empty_field,
                    highlightthickness=0,
                    bd=0,
                    activebackground=BACKGROUND,
                ))
                self.board_buttons[len(self.board_buttons) - 1].grid(row=row_id, column=column_id)

        # Add function to all buttons.
        self.board_buttons[0].config(command=lambda: self.press_move_button(0, (0, 0)))
        self.board_buttons[1].config(command=lambda: self.press_move_button(1, (0, 1)))
        self.board_buttons[2].config(command=lambda: self.press_move_button(2, (0, 2)))
        self.board_buttons[3].config(command=lambda: self.press_move_button(3, (1, 0)))
        self.board_buttons[4].config(command=lambda: self.press_move_button(4, (1, 1)))
        self.board_buttons[5].config(command=lambda: self.press_move_button(5, (1, 2)))
        self.board_buttons[6].config(command=lambda: self.press_move_button(6, (2, 0)))
        self.board_buttons[7].config(command=lambda: self.press_move_button(7, (2, 1)))
        self.board_buttons[8].config(command=lambda: self.press_move_button(8, (2, 2)))

        # Loop GUI
        self.root.mainloop()

    def press_move_button(self, button_id, xy):
        if not board.is_game_over():
            # Player turn
            board.make_move(xy[0], xy[1])
            button_image = PhotoImage(file=board.whose_turn())
            self.board_buttons[button_id].configure(image=button_image)
            self.board_buttons[button_id].image = button_image
            self.root.update()

            # Enemy turn
            if not board.is_game_over():
                move = enemy.make_move(board)
                board.make_move(*move)
                button_image = PhotoImage(file=board.whose_turn())
                self.board_buttons[move[0] * 3 + move[1]].configure(image=button_image)
                self.board_buttons[move[0] * 3 + move[1]].image = button_image
                self.root.update()

        # Inform player that game is over
        if board.is_game_over():
            messagebox.showinfo("Game over!", "Wohhoo game is over!")
