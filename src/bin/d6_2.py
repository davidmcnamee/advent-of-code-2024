from itertools import cycle

# raw_input = """....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#..."""


def main():
    raw_input = open("inputs/d6").read()
    board = [list(line) for line in raw_input.splitlines()]
    m, n = len(board), len(board[0])
    count = 0
    for i in range(m):
        for j in range(n):
            if board[i][j] == ".":
                board[i][j] = "#"
                if is_loop(board):
                    count += 1
                board[i][j] = "."
    print(count)


def is_loop(board):
    m, n = len(board), len(board[0])
    for x in range(m):
        for y in range(n):
            if board[x][y] == "^":
                i, j = x, y

    directions = cycle([(-1, 0), (0, 1), (1, 0), (0, -1)])
    cur_dir = next(directions)
    visited = set([(i, j, cur_dir)])
    while True:
        x, y = i + cur_dir[0], j + cur_dir[1]
        if not (0 <= x < m and 0 <= y < n):
            break
        if (x, y, cur_dir) in visited:
            return True
        if board[x][y] == "#":
            cur_dir = next(directions)
        else:
            i, j = x, y
            visited.add((i, j, cur_dir))
    return False


if __name__ == "__main__":
    main()
