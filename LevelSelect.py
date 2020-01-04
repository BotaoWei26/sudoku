from Graphics import Graphics
from tkinter import *
from random import randint

class LevelSelect:
    def __init__(self, window, ts):
        self.ts = ts
        self.window = window
        self.window.title("Sudoku")

        self.easy_button = Button(text="Easy", command=self.make_easy)
        self.medium_button = Button(text="Medium", command=self.make_medium)
        self.hard_button = Button(text="Hard", command=self.make_hard)
        self.vhard_button = Button(text="Very Hard", command=self.make_vhard)
        self.easy_button.grid()
        self.medium_button.grid()
        self.hard_button.grid()
        self.vhard_button.grid()

        self.g = None

    def make_easy(self):
        name = "easy" + str(randint(1, 3))
        board_file = open("boards/" + name + ".txt", "r")
        b = list(filter(lambda x: len(x) != 0, [list(map(int, filter(lambda x: x != '\n', line.split(" ")))) for line in board_file]))
        board_file.close()
        self.make_board(b, name)

    def make_medium(self):
        name = "medium" + str(randint(1, 3))
        board_file = open("boards/" + name + ".txt", "r")
        b = list(filter(lambda x: len(x) != 0, [list(map(int, filter(lambda x: x != '\n', line.split(" ")))) for line in board_file]))
        board_file.close()
        self.make_board(b, name)

    def make_hard(self):
        name = "hard" + str(randint(1, 3))
        board_file = open("boards/" + name + ".txt", "r")
        b = list(filter(lambda x: len(x) != 0, [list(map(int, filter(lambda x: x != '\n', line.split(" ")))) for line in board_file]))
        board_file.close()
        self.make_board(b, name)

    def make_vhard(self):
        name = "vhard" + str(randint(1, 1))
        board_file = open("boards/" + name + ".txt", "r")
        b = list(filter(lambda x: len(x) != 0, [list(map(int, filter(lambda x: x != '\n', line.split(" ")))) for line in board_file]))
        board_file.close()
        self.make_board(b, name)

    def make_board(self, b, name):
        game_window = Toplevel()
        self.g = Graphics(game_window, self.ts, b ,name)
