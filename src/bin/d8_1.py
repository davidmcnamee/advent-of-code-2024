from collections import defaultdict
from itertools import product

raw_input = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""


def main():
    raw_input = open("inputs/d8").read()
    board = [line for line in raw_input.strip().split("\n")]
    m, n = len(board), len(board[0])
    antennas = defaultdict(list)
    for i, row in enumerate(board):
        for j, c in enumerate(row):
            if c != ".":
                antennas[c].append((i, j))
    antinode_locations = set()

    for a_type, antenna_group in antennas.items():
        # print("antenna group", antenna_group)
        for (a, b), (c, d) in product(antenna_group, repeat=2):
            if (a, b) == (c, d):
                continue
            x, y = a - c, b - d
            antinode = (a - 2 * x, b - 2 * y)
            if (0 <= antinode[0] < m) and (0 <= antinode[1] < n):
                # print((a, b), (c, d), (x, y), antinode)
                antinode_locations.add(antinode)
        # print(a_type, len(antinode_locations))

    print(len(antinode_locations))


if __name__ == "__main__":
    main()
