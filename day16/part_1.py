from enum import Enum
from typing import NamedTuple


class Cords(NamedTuple):
    i: int
    j: int


class Direction(Enum):
    DOWN = "DOWN"
    UP = "UP"
    LEFT = "LEFT"
    RIGHT = "RIGHT"


def travel(layout: list[list[str]]) -> list[tuple[Cords, Direction]]:
    start_cords = Cords(0, 0)
    start_direction = Direction.RIGHT
    visited_cords = [(start_cords, start_direction)]

    cords_for_visit = [
        (get_next_cords(start_cords, direction), direction)
        for direction in get_directions(
            start_direction, layout[start_cords.i][start_cords.j]
        )
    ]
    while cords_for_visit:
        cur_cords, cur_direction = cords_for_visit.pop(0)

        if (cur_cords, cur_direction) in visited_cords:
            continue

        if is_out_of_bounds(layout, cur_cords):
            continue

        visited_cords.append((cur_cords, cur_direction))

        tile = layout[cur_cords.i][cur_cords.j]
        tile_directions = get_directions(cur_direction, tile)
        for tile_direction in tile_directions:
            cords_for_visit.append(
                (get_next_cords(cur_cords, tile_direction), tile_direction)
            )

    return visited_cords


def is_out_of_bounds(layout: list[list[str]], cords: Cords):
    return (
        cords.i < 0
        or cords.i > len(layout) - 1
        or cords.j < 0
        or cords.j > len(layout[0]) - 1
    )


def get_next_cords(current: Cords, direction: Direction):
    if direction == Direction.DOWN:
        return Cords(current.i + 1, current.j)
    elif direction == Direction.UP:
        return Cords(current.i - 1, current.j)
    elif direction == Direction.RIGHT:
        return Cords(current.i, current.j + 1)
    elif direction == Direction.LEFT:
        return Cords(current.i, current.j - 1)


def get_directions(current_direction: Direction, tile: "str") -> list[Direction]:
    directions_map = {
        ".": {},
        "|": {
            Direction.RIGHT: [Direction.UP, Direction.DOWN],
            Direction.LEFT: [Direction.UP, Direction.DOWN],
        },
        "-": {
            Direction.RIGHT: [Direction.RIGHT],
            Direction.LEFT: [Direction.LEFT],
            Direction.UP: [Direction.LEFT, Direction.RIGHT],
            Direction.DOWN: [Direction.LEFT, Direction.RIGHT],
        },
        "\\": {
            Direction.RIGHT: [Direction.DOWN],
            Direction.LEFT: [Direction.UP],
            Direction.UP: [Direction.LEFT],
            Direction.DOWN: [Direction.RIGHT],
        },
        "/": {
            Direction.RIGHT: [Direction.UP],
            Direction.LEFT: [Direction.DOWN],
            Direction.UP: [Direction.RIGHT],
            Direction.DOWN: [Direction.LEFT],
        },
    }

    return directions_map[tile].get(current_direction, [current_direction])


def main():
    with open("input.txt", "r") as file:
        data = file.read()

    layout = list(map(list, data.splitlines()))
    visited = travel(layout)
    visited_cords = set([cords for cords, _ in visited])

    print(len(visited_cords))


if __name__ == "__main__":
    main()
