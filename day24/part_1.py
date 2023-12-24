from itertools import combinations
from typing import NamedTuple


class Cords(NamedTuple):
    x: int
    y: int
    z: int


class Track(NamedTuple):
    start: Cords
    end: Cords
    velocity: Cords


TEST_AREA_BOUND = (200000000000000, 400000000000000)


def is_intersects(track_1: Track, track_2: Track) -> tuple[int, int] | None:
    xdiff = (track_1.start.x - track_1.end.x, track_2.start.x - track_2.end.x)
    ydiff = (track_1.start.y - track_1.end.y, track_2.start.y - track_2.end.y)

    def det(a: tuple[int], b: tuple[int]):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        return None

    d = (det(track_1.start, track_1.end), det(track_2.start, track_2.end))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div

    if (
        (track_1.velocity.x > 0 and track_1.start.x > x)
        or (track_1.velocity.x < 0 and track_1.start.x < x)
        or (track_2.velocity.x > 0 and track_2.start.x > x)
        or (track_2.velocity.x < 0 and track_2.start.x < x)
    ):
        return None

    if (
        (track_1.velocity.y > 0 and track_1.start.y > y)
        or (track_1.velocity.y < 0 and track_1.start.y < y)
        or (track_2.velocity.y > 0 and track_2.start.y > y)
        or (track_2.velocity.y < 0 and track_2.start.y < y)
    ):
        return None

    if not (TEST_AREA_BOUND[0] < x < TEST_AREA_BOUND[1]) or not (
        TEST_AREA_BOUND[0] < y < TEST_AREA_BOUND[1]
    ):
        return None

    return x, y


def main():
    with open("day24/input.txt", "r") as file:
        data = file.read()

    tracks = []
    for hailstone in data.splitlines():
        current, velocity = hailstone.split(" @ ")

        start_cords = Cords(*map(int, current.split(",")))
        velocity_cords = Cords(*map(int, velocity.split(",")))
        end_cords = Cords(
            start_cords.x + velocity_cords.x,
            start_cords.y + velocity_cords.y,
            start_cords.z + velocity_cords.z,
        )

        tracks.append(
            Track(
                start_cords,
                end_cords,
                velocity_cords,
            )
        )

    intersections_count = 0
    for t1, t2 in combinations(tracks, 2):
        if is_intersects(t1, t2) is not None:
            intersections_count += 1

    print(intersections_count)


if __name__ == "__main__":
    main()
