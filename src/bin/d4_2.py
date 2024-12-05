# cerces search (part 2)
from typing import Generator


def scan_for_xmas(board: list[str], positions: list[tuple[int, int]]) -> str:
    def inner(
        board: list[str], positions: list[tuple[int, int]]
    ) -> Generator[str | None, None, None]:
        m, n = len(board), len(board[0])
        for i, j in positions:
            if not (0 <= i < m and 0 <= j < n):
                yield None
            else:
                yield board[i][j]

    return "".join([c for c in inner(board, positions) if c is not None])


def look_around(board: list[str], i: int, j: int) -> Generator[int, None, None]:
    # diagonals
    d1 = scan_for_xmas(board, [(i - 1, j - 1), (i, j), (i + 1, j + 1)]) == "MAS"
    d2 = scan_for_xmas(board, [(i - 1, j + 1), (i, j), (i + 1, j - 1)]) == "MAS"
    d3 = scan_for_xmas(board, [(i + 1, j - 1), (i, j), (i - 1, j + 1)]) == "MAS"
    d4 = scan_for_xmas(board, [(i + 1, j + 1), (i, j), (i - 1, j - 1)]) == "MAS"

    if sum([d1, d2, d3, d4]) >= 2:
        yield 1


def main():
    with open("inputs/d4") as f:
        board = f.read().strip().splitlines()
    m, n = len(board), len(board[0])
    total = 0
    for i in range(m):
        for j in range(n):
            total += sum(look_around(board, i, j))
    print(total)


if __name__ == "__main__":
    main()
