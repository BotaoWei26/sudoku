from copy import deepcopy
from solveFunctions import solve_generator

class Sudoku:
    def __init__(self):
        #self.board = [[0 for i in range(9)] for i in range(9)]

        self.board =[[0, 4, 0, 0, 0, 0, 1, 7, 9],
                     [0, 0, 2, 0, 0, 8, 0, 5, 4],
                     [0, 0, 6, 0, 0, 5, 0, 0, 8],
                     [0, 8, 0, 0, 7, 0, 9, 1, 0],
                     [0, 5, 0, 0, 9, 0, 0, 3, 0],
                     [0, 1, 9, 0, 6, 0, 0, 4, 0],
                     [3, 0, 0, 4, 0, 0, 7, 0, 0],
                     [5, 7, 0, 1, 0, 0, 2, 0, 0],
                     [9, 2, 8, 0, 0, 0, 0, 6, 0]]

        self.curr_board = deepcopy(self.board)

        self.selected = []

        self.red = []

    def fill(self, row, col, val):
        self.curr_board[row][col] = val
        self.deselect()
        self.check_red()

    def select(self, x, y):
        self.selected = [x, y]

    def deselect(self):
        self.selected = []

    def check_red(self):
        self.red = []
        for row in range(9):
            for col in range(9):
                num = self.curr_board[row][col]
                if num == 0:
                    continue
                start_row = (row // 3) * 3
                start_col = (col // 3) * 3
                test1 = self.curr_board[row]
                test2 = [self.curr_board[r][col] for r in range(9)]
                test3 = [self.curr_board[r][c] for r in range(start_row, start_row + 3) for c in range(start_col, start_col + 3)]
                if self.curr_board[row].count(num) >= 2 or \
                [self.curr_board[r][col] for r in range(9)].count(num) >= 2 or \
                [self.curr_board[r][c] for r in range(start_row, start_row + 3) for c in range(start_col, start_col + 3)].count(num) >= 2:
                    self.red.append([row, col])


    def solve_board(self):
        for b in solve_generator(self.board):
            yield b
