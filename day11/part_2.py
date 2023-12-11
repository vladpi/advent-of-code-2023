from itertools import combinations
from typing import NamedTuple


class Cords(NamedTuple):
    i: int
    j: int


def get_galactics_cords(data: list[str]) -> list[Cords]:
    cords = []

    for i, row in enumerate(data):
        for j, cell in enumerate(row):
            if cell == "#":
                cords.append(Cords(i, j))

    return cords


def get_empty_rows(data: list[str]) -> list[int]:
    return [i for i, row in enumerate(data) if row.count("#") == 0]


def get_empty_cols(data: list[str]) -> list[int]:
    empty_cols = []

    for j in range(len(data[0])):
        if not any([data[i][j] for i in range(len(data)) if data[i][j] != "."]):
            empty_cols.append(j)

    return empty_cols


def get_distance(
    a: Cords,
    b: Cords,
    empty_rows: list[int],
    empty_cols: list[int],
) -> int:
    rows = sum([1000000 - 1 for i in empty_rows if min(a.i, b.i) < i < max(a.i, b.i)])
    cols = sum([1000000 - 1 for j in empty_cols if min(a.j, b.j) < j < max(a.j, b.j)])

    return abs(b.j - a.j) + cols + abs(b.i - a.i) + rows


def main():
    with open("input.txt", "r") as file:
        data = file.read().splitlines()

    galactics_cords = get_galactics_cords(data)
    empty_rows = get_empty_rows(data)
    empty_cols = get_empty_cols(data)

    result = 0
    for a, b in combinations(galactics_cords, 2):
        result += get_distance(a, b, empty_rows, empty_cols)

    print(result)


if __name__ == "__main__":
    main()
