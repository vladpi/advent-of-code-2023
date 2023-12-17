from heapq import heappop, heappush
from typing import NamedTuple


class Point(NamedTuple):
    total_heat: int
    i: int
    j: int
    direction: tuple[int, int]
    direction_counter: int


def find_optimal_heat_loss(city_map: list[list[int]]) -> int:
    finish = (len(city_map) - 1, len(city_map[0]) - 1)
    visited = set()
    for_visit = [Point(0, 0, 0, (0, 0), 0)]

    while for_visit:
        point = heappop(for_visit)

        if (point.i, point.j) == finish and point.direction_counter >= 4:
            return point.total_heat

        if (point.i, point.j, point.direction, point.direction_counter) in visited:
            continue

        visited.add((point.i, point.j, point.direction, point.direction_counter))

        if point.direction_counter < 10 and point.direction != (0, 0):
            i_direction, j_direction = point.direction
            check_and_push_point(
                city_map,
                for_visit,
                point.total_heat,
                point.i + i_direction,
                point.j + j_direction,
                point.direction,
                point.direction_counter,
            )

        if point.direction_counter >= 4 or point.direction == (0, 0):
            for new_direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if new_direction == point.direction or new_direction == (
                    -point.direction[0],
                    -point.direction[1],
                ):
                    continue

                i_direction, j_direction = new_direction
                check_and_push_point(
                    city_map,
                    for_visit,
                    point.total_heat,
                    point.i + i_direction,
                    point.j + j_direction,
                    new_direction,
                )

    return -1


def check_and_push_point(
    city_map: list[list[int]],
    for_visit: list[Point],
    init_heat: int,
    i: int,
    j: int,
    direction: tuple[int, int],
    init_direction_count: int = 0,
):
    if not is_out_of_bounds(city_map, i, j):
        heappush(
            for_visit,
            Point(
                init_heat + city_map[i][j],
                i,
                j,
                direction,
                init_direction_count + 1,
            ),
        )


def is_out_of_bounds(city_map: list[list[int]], i: int, j: int) -> bool:
    return i < 0 or i > len(city_map) - 1 or j < 0 or j > len(city_map[0]) - 1


def main():
    with open("input.txt", "r") as file:
        data = file.read()

    city_map = [list(map(int, line)) for line in data.splitlines()]
    res = find_optimal_heat_loss(city_map)

    print(res)


if __name__ == "__main__":
    main()
