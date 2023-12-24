from typing import NamedTuple

STEPS_LIMIT = 64


class Cords(NamedTuple):
    i: int
    j: int


def find_start_cords(garden_map: list[list[str]]) -> Cords:
    for i, row in enumerate(garden_map):
        try:
            return Cords(i, row.index("S"))
        except ValueError:
            continue


def get_next_cords(
    garden_map: list[list[str]], starts_cords: list[Cords]
) -> list[Cords]:
    next_starts_cords = []
    for cords in starts_cords:
        next_starts_cords += get_plots_around(garden_map, cords)
    return list(set(next_starts_cords))


def get_plots_around(garden_map: list[list[str]], cords: Cords) -> list[Cords]:
    plots_around = []
    for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        plot_cords = Cords(cords.i + i, cords.j + j)
        if (
            not is_out_of_bounds(garden_map, plot_cords)
            and garden_map[plot_cords.i][plot_cords.j] != "#"
        ):
            plots_around.append(plot_cords)
    return plots_around


def is_out_of_bounds(garden_map: list[list[str]], cords: Cords):
    return (
        cords.i < 0
        or cords.i > len(garden_map) - 1
        or cords.j < 0
        or cords.j > len(garden_map[0]) - 1
    )


def main():
    with open("day21/input.txt", "r") as file:
        data = file.read()

    garden_map = [list(s) for s in data.splitlines()]

    steps_count = 0
    next_cords = [find_start_cords(garden_map)]
    while steps_count != STEPS_LIMIT:
        steps_count += 1
        next_cords = get_next_cords(garden_map, next_cords)
    print(len(next_cords))


if __name__ == "__main__":
    main()
