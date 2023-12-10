def find_s_position(data: list[str]) -> tuple[int, int]:
    for i, row in enumerate(data):
        try:
            j = row.index("S")
            return (i, j)
        except ValueError:
            continue

def find_s_ouputs(data: list[str], s_i: int, s_j: int) -> list[tuple[int, int]]:
    ouputs = []

    for i_coef, j_coef in [
        (-1, -1),
        (-1, 0),
        (-1, +1),
        (0, -1),
        (0, +1),
        (+1, -1),
        (+1, 0),
        (+1, +1),
    ]:
        pipe = get_pipe(data, s_i + i_coef, s_j + j_coef)
        if pipe is not None:
            pipe_coefs = get_input_ouput(pipe, s_i + i_coef, s_j + j_coef)
            if (s_i, s_j) in pipe_coefs:
                ouputs.append((s_i + i_coef, s_j + j_coef))

    return ouputs


def get_pipe(data: list[str], i: int, j: int) -> str | None:
    try:
        return data[i][j]
    except IndexError:
        return None


def get_input_ouput(pipe: str, i: int, j: int) -> list[tuple[int, int]]:
    coefs_map = {
        "|": [(i - 1, j), (i + 1, j)],
        "-": [(i, j - 1), (i, j + 1)],
        "L": [(i - 1, j), (i, j + 1)],
        "J": [(i - 1, j), (i, j - 1)],
        "7": [(i, j - 1), (i + 1, j)],
        "F": [(i, j + 1), (i + 1, j)],
        ".": [],
    }
    return coefs_map[pipe]


def get_next_pipe(
    data: list[str], cur: tuple[int, int], prev: tuple[int]
) -> tuple[int, int] | None:
    i, j = cur
    pipe = data[i][j]
    next_pipes = get_input_ouput(pipe, i, j)
    for p in next_pipes:
        if p != prev:
            return p
    return None


def main():
    with open("input.txt", "r") as file:
        data = file.read().splitlines()

    s_i, s_j = find_s_position(data)
    s_ouputs = find_s_ouputs(data, s_i, s_j)

    first_prev, second_prev = (s_i, s_j), (s_i, s_j)
    first_pos, second_pos, *_ = s_ouputs
    steps_count = 1
    while first_pos != second_pos:
        first_pos, first_prev = get_next_pipe(data, first_pos, first_prev), first_pos
        second_pos, second_prev = get_next_pipe(data, second_pos, second_prev), second_pos
        steps_count += 1

    print(steps_count)


if __name__ == "__main__":
    main()
