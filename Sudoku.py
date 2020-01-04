from copy import deepcopy
from solveFunctions import solve_generator, valid_board

class Sudoku:
    def __init__(self, b):

        self.board = b

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

    def isFinished(self):
        return valid_board(self.curr_board)
