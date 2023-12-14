def roll_north(data: list[list[str]]) -> list[list[str]]:
    for j in range(len(data[0])):
        empty_cells = []

        for i in range(len(data)):
            if data[i][j] == ".":
                empty_cells.append(i)
            if data[i][j] == "#":
                empty_cells = []
            if data[i][j] == "O" and empty_cells:
                new_i = min(empty_cells)
                data[i][j] = "."
                data[new_i][j] = "O"
                empty_cells.remove(new_i)
                empty_cells.append(i)

    return data


def roll_west(data: list[list[str]]) -> list[list[str]]:
    for i in range(len(data)):
        empty_cells = []

        for j in range(len(data[0])):
            if data[i][j] == ".":
                empty_cells.append(j)
            if data[i][j] == "#":
                empty_cells = []
            if data[i][j] == "O" and empty_cells:
                new_j = min(empty_cells)
                data[i][j] = "."
                data[i][new_j] = "O"
                empty_cells.remove(new_j)
                empty_cells.append(j)

    return data


def roll_south(data: list[list[str]]) -> list[list[str]]:
    for j in range(len(data[0])):
        empty_cells = []

        for i in range(len(data) - 1, -1, -1):
            if data[i][j] == ".":
                empty_cells.append(i)
            if data[i][j] == "#":
                empty_cells = []
            if data[i][j] == "O" and empty_cells:
                new_i = max(empty_cells)
                data[i][j] = "."
                data[new_i][j] = "O"
                empty_cells.remove(new_i)
                empty_cells.append(i)

    return data


def roll_east(data: list[list[str]]) -> list[list[str]]:
    for i in range(len(data)):
        empty_cells = []

        for j in range(len(data[0]) - 1, -1, -1):
            if data[i][j] == ".":
                empty_cells.append(j)
            if data[i][j] == "#":
                empty_cells = []
            if data[i][j] == "O" and empty_cells:
                new_j = max(empty_cells)
                data[i][j] = "."
                data[i][new_j] = "O"
                empty_cells.remove(new_j)
                empty_cells.append(j)

    return data


def make_cycle(data: list[list[str]]) -> list[list[str]]:
    data = roll_north(data)
    data = roll_west(data)
    data = roll_south(data)
    data = roll_east(data)
    return data


def calc_load(data: list[list[str]]) -> int:
    load = 0
    for idx, row in enumerate(data):
        load += row.count("O") * (len(data) - idx)
    return load


def to_hashable(data: list[list[int]]) -> tuple[tuple[str]]:
    return tuple(tuple(row) for row in data)


def main():
    with open("input.txt", "r") as file:
        data = file.read().splitlines()

    for idx, row in enumerate(data):
        data[idx] = list(row)

    history = [to_hashable(data)]

    i = 0
    while True:
        i += 1
        data = make_cycle(data)
        hash_data = to_hashable(data)
        if hash_data in history:
            break
        history.append(hash_data)

    first = history.index(to_hashable(data))
    result = calc_load(history[(1000000000 - first) % (i - first) + first])
    print(result)


if __name__ == "__main__":
    main()
