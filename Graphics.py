from tkinter import *
from Sudoku import *
from time import sleep

class Graphics:
    def __init__(self, window, ts, b, name):
        self.ts = ts
        self.window = window
        self.sudoku = Sudoku(b)

        self.window.title("Sudoku " + name)
        self.window.geometry(str(self.ts * 11) + "x" + str(self.ts * 11))

        self.beige_numbers = {
            "0": PhotoImage(file="sprites/beige0.gif"),
            "1": PhotoImage(file="sprites/beige1.gif"),
            "2": PhotoImage(file="sprites/beige2.gif"),
            "3": PhotoImage(file="sprites/beige3.gif"),
            "4": PhotoImage(file="sprites/beige4.gif"),
            "5": PhotoImage(file="sprites/beige5.gif"),
            "6": PhotoImage(file="sprites/beige6.gif"),
            "7": PhotoImage(file="sprites/beige7.gif"),
            "8": PhotoImage(file="sprites/beige8.gif"),
            "9": PhotoImage(file="sprites/beige9.gif")
        }
        self.yellow_numbers = {
            "0": PhotoImage(file="sprites/yellow0.gif"),
            "1": PhotoImage(file="sprites/yellow1.gif"),
            "2": PhotoImage(file="sprites/yellow2.gif"),
            "3": PhotoImage(file="sprites/yellow3.gif"),
            "4": PhotoImage(file="sprites/yellow4.gif"),
            "5": PhotoImage(file="sprites/yellow5.gif"),
            "6": PhotoImage(file="sprites/yellow6.gif"),
            "7": PhotoImage(file="sprites/yellow7.gif"),
            "8": PhotoImage(file="sprites/yellow8.gif"),
            "9": PhotoImage(file="sprites/yellow9.gif")
        }
        self.red_numbers = {
            "0": PhotoImage(file="sprites/red0.gif"),
            "1": PhotoImage(file="sprites/red1.gif"),
            "2": PhotoImage(file="sprites/red2.gif"),
            "3": PhotoImage(file="sprites/red3.gif"),
            "4": PhotoImage(file="sprites/red4.gif"),
            "5": PhotoImage(file="sprites/red5.gif"),
            "6": PhotoImage(file="sprites/red6.gif"),
            "7": PhotoImage(file="sprites/red7.gif"),
            "8": PhotoImage(file="sprites/red8.gif"),
            "9": PhotoImage(file="sprites/red9.gif")
        }
        self.blue_numbers = {
            "0": PhotoImage(file="sprites/blue0.gif"),
            "1": PhotoImage(file="sprites/blue1.gif"),
            "2": PhotoImage(file="sprites/blue2.gif"),
            "3": PhotoImage(file="sprites/blue3.gif"),
            "4": PhotoImage(file="sprites/blue4.gif"),
            "5": PhotoImage(file="sprites/blue5.gif"),
            "6": PhotoImage(file="sprites/blue6.gif"),
            "7": PhotoImage(file="sprites/blue7.gif"),
            "8": PhotoImage(file="sprites/blue8.gif"),
            "9": PhotoImage(file="sprites/blue9.gif")
        }
        self.green_numbers = {
            "0": PhotoImage(file="sprites/green0.gif"),
            "1": PhotoImage(file="sprites/green1.gif"),
            "2": PhotoImage(file="sprites/green2.gif"),
            "3": PhotoImage(file="sprites/green3.gif"),
            "4": PhotoImage(file="sprites/green4.gif"),
            "5": PhotoImage(file="sprites/green5.gif"),
            "6": PhotoImage(file="sprites/green6.gif"),
            "7": PhotoImage(file="sprites/green7.gif"),
            "8": PhotoImage(file="sprites/green8.gif"),
            "9": PhotoImage(file="sprites/green9.gif")
        }

        self.blank_sprite = PhotoImage("sprites/blank.gif")
        self.tiles = [[None for j in range(9)] for i in range(9)]
        for i in range(9):
            for j in range(9):
                self.tiles[i][j] = Label(self.window, height=self.ts, width=self.ts, bg="white", borderwidth=1, relief="solid")
                self.tiles[i][j].grid(row=i, column=j)

        self.solve_button = Button(self.window, text="Solve", command=self.solve_setup)
        self.solve_button.grid(row=9, column=9)

        self.board_generator = self.sudoku.solve_board()
        self.draw_board()

    def solve_setup(self):
        self.window.unbind("<Key>")
        for i in range(9):
            for j in range(9):
                self.tiles[i][j].unbind('<Button-1>')
        self.solve()

    def solve(self):
        try:
            b = next(self.board_generator)
            for i in range(9):
                for j in range(9):
                    if b[i][j] != 0 and b[i][j] == self.sudoku.board[i][j]:
                        continue
                    if b[i][j] == 0:
                        sprite = self.beige_numbers[str(b[i][j])]
                    else:
                        sprite = self.yellow_numbers[str(b[i][j])]
                    self.tiles[i][j].config(image=sprite)
            self.window.after_idle(func=self.solve)
        except StopIteration:
            pass

    def draw_board(self):
        self.window.unbind("<Key>")
        for i in range(9):
            for j in range(9):
                self.tiles[i][j].unbind('<Button-1>')
                if [i, j] == self.sudoku.selected:
                    sprite = self.green_numbers[str(self.sudoku.curr_board[i][j])]
                    self.window.bind("<Key>", self.num_press(i, j))
                elif self.sudoku.curr_board[i][j] == self.sudoku.board[i][j] and [i, j] in self.sudoku.red:
                    sprite = self.blue_numbers[str(self.sudoku.curr_board[i][j])]
                elif [i, j] in self.sudoku.red:
                    sprite = self.red_numbers[str(self.sudoku.curr_board[i][j])]
                    self.tiles[i][j].bind('<Button-1>', self.click(i, j))
                elif self.sudoku.board[i][j] != 0 and self.sudoku.curr_board[i][j] == self.sudoku.board[i][j]:
                    sprite = self.yellow_numbers[str(self.sudoku.curr_board[i][j])]
                else:
                    sprite = self.beige_numbers[str(self.sudoku.curr_board[i][j])]
                    self.tiles[i][j].bind('<Button-1>', self.click(i, j))
                self.tiles[i][j].config(image=sprite)

    def draw_finished(self):
        self.window.unbind("<Key>")
        for i in range(9):
            for j in range(9):
                self.tiles[i][j].unbind('<Button-1>')
                sprite = self.yellow_numbers[str(self.sudoku.curr_board[i][j])]
                self.tiles[i][j].config(image=sprite)

    def click(self, x, y):
        return lambda event: self.select(x, y)

    def num_press(self, x, y):
        return lambda event: self.change(x, y, event.char)

    def select(self, x, y):
        self.sudoku.select(x, y)
        self.draw_board()

    def change(self, x, y, num):
        if str.isdigit(num):
            self.sudoku.fill(x, y, int(num))

        if self.sudoku.isFinished():
            self.draw_finished()
        else:
            self.draw_board()
