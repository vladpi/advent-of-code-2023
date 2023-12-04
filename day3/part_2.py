from collections import defaultdict
from typing import NamedTuple


class Symbol(NamedTuple):
    symbol: str
    i: int
    j: int


def is_part_number(data: list[str], i: int, j: int) -> bool:
    return bool(get_all_symbols(data, i, j))


def get_gear_symbols(data: list[str], i: int, j: int) -> list[Symbol]:
    return list(filter(lambda x: x.symbol == "*", get_all_symbols(data, i, j)))


def get_all_symbols(data: list[str], i: int, j: int) -> list[Symbol]:
    return list(
        filter(
            None,
            [
                get_symbol(data, i + 1, j),
                get_symbol(data, i - 1, j),
                get_symbol(data, i, j + 1),
                get_symbol(data, i, j - 1),
                get_symbol(data, i + 1, j + 1),
                get_symbol(data, i + 1, j - 1),
                get_symbol(data, i - 1, j + 1),
                get_symbol(data, i - 1, j - 1),
            ],
        )
    )


def get_symbol(data: list[str], i: int, j: int) -> Symbol | None:
    try:
        symbol = data[i][j]
    except IndexError:
        return None

    if symbol != "." and not symbol.isdigit():
        return Symbol(symbol, i, j)

    return None


def main():
    with open("input.txt", "r") as file:
        data = file.read().splitlines()

    gears: dict[Symbol, list[int]] = defaultdict(list)

    curr_part_number = ""
    curr_gears_symbols = []
    for ridx, row in enumerate(data):
        for sidx, symb in enumerate(row):
            if symb.isdigit():
                curr_part_number += symb
                curr_gears_symbols += get_gear_symbols(data, ridx, sidx)

            else:
                if curr_part_number:
                    for s in set(curr_gears_symbols):
                        gears[s].append(int(curr_part_number))
                    curr_part_number, curr_gears_symbols = "", []

        if curr_part_number:
            for s in set(curr_gears_symbols):
                gears[s].append(int(curr_part_number))
            curr_part_number, curr_gears_symbols = "", []

    result = 0
    for gears_part_numbers in gears.values():
        if len(gears_part_numbers) != 2:
            continue
        result += gears_part_numbers[0] * gears_part_numbers[1]
    print(result)


if __name__ == "__main__":
    main()
