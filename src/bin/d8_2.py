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
        for (a, b), (c, d) in product(antenna_group, repeat=2):
            if (a, b) == (c, d):
                continue
            x, y = a - c, b - d
            i = 0
            while (
                (antinode := (a - i * x, b - i * y))
                and (0 <= antinode[0] < m)
                and (0 <= antinode[1] < n)
            ):
                antinode_locations.add(antinode)
                i += 1

    print(len(antinode_locations))


if __name__ == "__main__":
    main()
