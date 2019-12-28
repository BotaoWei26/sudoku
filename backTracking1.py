from copy import deepcopy


def solve(b):
    return solve_rec(b, 81 - 1)


def solve_rec(b, square):
    if square == -1:
        # checked last square
        return b

    row = (square // 9)
    col = (square % 9)
    if b[row][col] != 0:
        # square value is not 0
        return solve_rec(b, square - 1)

    b = deepcopy(b)
    test = deepcopy(b)
    for guess in range(9):
        test[row][col] = guess + 1
        if valid_board(test):
            rec_b = solve_rec(test, square - 1)
            if complete_board(rec_b) and valid_board(rec_b):
                return rec_b
    return b


def valid_board(b):
    for row in range(9):
        if not valid_group(b[row]):
            return False
    for col in range(9):
        if not valid_group([b[row][col] for row in range(9)]):
            return False
    for square in range(9):
        start_row = (square // 3) * 3
        start_col = (square % 3) * 3
        if not valid_group([b[row][col] for row in range(start_row, start_row + 3) for col in range(start_col, start_col + 3)]):
            return False
    return True


def valid_group(g):
    return all(g.count(i+1) <= 1 for i in range(9))


def complete_board(b):
    return all(s != 0 for row in b for s in row)


def format_board(file_name):
    board_file = open("boards/" + file_name + ".txt", "r")
    return list(filter(lambda x: len(x) != 0, [list(map(int, filter(lambda x: x != '\n', line.split(" ")))) for line in board_file]))


file_name = input("File:")
board = format_board(file_name)
print(board)
print(solve(board))
