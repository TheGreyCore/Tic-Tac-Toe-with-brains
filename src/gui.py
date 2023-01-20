from tkinter import Tk, Button


def create_board_buttons(root):
    board_buttons = []
    for column_id in range(0, 3):
        row = []
        for row_id in range(0, 3):
            row.append(Button(
                root,
                text="      .       ",
            ))
            row[row_id].grid(row=row_id, column=column_id)
        board_buttons.append(row)
    return board_buttons


class GUI:
    def __init__(self):
        print("Init")
        self.root = Tk()
        self.board_buttons = create_board_buttons(self.root)
        self.root.mainloop()
