from copy import deepcopy



def solve_generator(b):
    b_original = deepcopy(b)
    counter = 0
    last = []
    while counter < 81:
        row = (counter // 9)
        col = (counter % 9)
        if b_original[row][col] == 0:
            b[row][col] += 1
            last.append(counter)
            if b[row][col] > 9:
                b[row][col] = 0
                last.pop()
                counter = last.pop()
                continue
            yield b
            if valid_move(b, row, col):
                counter += 1
                continue
            else:
                counter = last.pop()
                continue
        else:
            counter += 1
            continue
    return


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
