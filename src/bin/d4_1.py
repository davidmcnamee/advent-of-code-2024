# cerces search (part 1)
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
    # vertical/horizontal
    if scan_for_xmas(board, [(i, j), (i + 1, j), (i + 2, j), (i + 3, j)]) == "XMAS":
        yield 1
    if scan_for_xmas(board, [(i, j), (i - 1, j), (i - 2, j), (i - 3, j)]) == "XMAS":
        yield 1
    if scan_for_xmas(board, [(i, j), (i, j - 1), (i, j - 2), (i, j - 3)]) == "XMAS":
        yield 1
    if scan_for_xmas(board, [(i, j), (i, j + 1), (i, j + 2), (i, j + 3)]) == "XMAS":
        yield 1
    # diagonals
    if (
        scan_for_xmas(board, [(i, j), (i + 1, j + 1), (i + 2, j + 2), (i + 3, j + 3)])
        == "XMAS"
    ):
        yield 1
    if (
        scan_for_xmas(board, [(i, j), (i - 1, j - 1), (i - 2, j - 2), (i - 3, j - 3)])
        == "XMAS"
    ):
        yield 1
    if (
        scan_for_xmas(board, [(i, j), (i - 1, j + 1), (i - 2, j + 2), (i - 3, j + 3)])
        == "XMAS"
    ):
        yield 1
    if (
        scan_for_xmas(board, [(i, j), (i + 1, j - 1), (i + 2, j - 2), (i + 3, j - 3)])
        == "XMAS"
    ):
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
