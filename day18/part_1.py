def calc_area(points: list[tuple[int, int]], len_of_edge: int) -> int:
    area = (
        abs(
            sum(
                points[i][0] * (points[i - 1][1] - points[(i + 1) % len(points)][1])
                for i in range(len(points))
            )
        )
        // 2
    )
    return (area - len_of_edge // 2 + 1) + len_of_edge


def main():
    with open("input.txt", "r") as file:
        data = file.read()

    points = [(0, 0)]
    len_of_edge = 0
    for instruction in data.splitlines():
        prev_point = points[-1]
        direction, meters, _ = instruction.split()
        meters = int(meters)
        len_of_edge += meters
        if direction == "R":
            points.append((prev_point[0], prev_point[1] + meters))
        elif direction == "L":
            points.append((prev_point[0], prev_point[1] - meters))
        elif direction == "D":
            points.append((prev_point[0] + meters, prev_point[1]))
        elif direction == "U":
            points.append((prev_point[0] - meters, prev_point[1]))

    print(calc_area(points, len_of_edge))


if __name__ == "__main__":
    main()
