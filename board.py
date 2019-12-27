board_file = open("boards/test1.in", "r")
board = list(map(lambda x: list(map(lambda y: y.strip('\n'), x)), [line.split(" ") for line in board_file]))
print(board)

