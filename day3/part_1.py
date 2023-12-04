def is_part_number(data: list[str], i: int, j: int) -> bool:
    return bool(get_all_symbols(data, i, j))


def get_all_symbols(data: list[str], i: int, j: int) -> list[str]:
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


def get_symbol(data: list[str], i: int, j: int) -> str | None:
    try:
        symbol = data[i][j]
    except IndexError:
        return None

    if symbol != "." and not symbol.isdigit():
        return symbol

    return None


def main():
    with open("input.txt", "r") as file:
        data = file.read().splitlines()

    part_numbers = []
    curr_part_number = ""
    curr_is_part_number = False
    for ridx, row in enumerate(data):
        for sidx, symb in enumerate(row):
            if symb.isdigit():
                curr_part_number += symb
                curr_is_part_number = curr_is_part_number or is_part_number(
                    data, ridx, sidx
                )

            else:
                if curr_part_number:
                    if curr_is_part_number:
                        part_numbers.append(curr_part_number)
                    curr_part_number, curr_is_part_number = "", False

        if curr_part_number:
            if curr_is_part_number:
                part_numbers.append(curr_part_number)
            curr_part_number, curr_is_part_number = "", False

    print(sum(map(int, part_numbers)))


if __name__ == "__main__":
    main()
