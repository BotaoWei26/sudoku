
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

    for guess in range(9):
        b[row][col] = guess + 1
        pretty_print_board(b)
        if valid_move(b, row, col):
            rec_b = solve_rec(b, square - 1)
            if complete_board(rec_b) and valid_move(rec_b, row, col):
                return rec_b

    b[row][col] = 0
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


def valid_move(b, row, col):
    if not valid_group(b[row]) or not valid_group([b[row][col] for row in range(9)]):
        return False
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    if not valid_group([b[row][col] for row in range(start_row, start_row + 3) for col in range(start_col, start_col + 3)]):
        return False
    return True


def valid_group(g):
    seen = []
    for i in g:
        if i != 0 and i in seen:
            return False
        else:
            seen.append(i)
    return True


def complete_board(b):
    return all(s != 0 for row in b for s in row)


def format_board(fn):
    board_file = open("boards/" + fn + ".txt", "r")
    return list(filter(lambda x: len(x) != 0, [list(map(int, filter(lambda x: x != '\n', line.split(" ")))) for line in board_file]))


def pretty_print_board(b):
    for row in b:
        for num in row:
            print(num, end='')
        print()
    print()


board = format_board(input("File:"))

pretty_print_board(board)
pretty_print_board(solve(board))
