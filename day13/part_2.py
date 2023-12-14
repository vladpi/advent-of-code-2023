def find_vertical_reflection(pattern: list[str]) -> int | None:
    cols_as_str = [get_cols_as_str(pattern, j) for j in range(len(pattern[0]))]
    return find_reflection(cols_as_str)


def find_reflection(pattern: list[str]) -> int | None:
    for i in range(len(pattern) - 1):
        if is_reflection(pattern, i):
            return i


def is_reflection(rows: list[str], i: int) -> bool:
    refl_len = min(len(rows) - (i + 1), i + 1)
    left_part = rows[i - refl_len + 1 : i + 1]
    right_part = list(reversed(rows[i + 1 : i + 1 + refl_len]))
    return count_diff(left_part, right_part) == 1


def count_diff(left_rows: list[str], right_rows: list[str]) -> int:
    diff = 0
    for left, right in zip(left_rows, right_rows):
        for i, j in zip(left, right):
            if i != j:
                diff += 1
    return diff


def get_cols_as_str(pattern: list[str], col: int) -> str:
    return "".join([pattern[i][col] for i in range(len(pattern))])


def main():
    with open("input.txt", "r") as file:
        data = file.read()

    patterns = data.split("\n\n")

    reflections = []
    for idx, p in enumerate(patterns):
        vert_reflection = find_vertical_reflection(p.splitlines())
        if vert_reflection is not None:
            reflections.append(vert_reflection + 1)

        horiz_reflection = find_reflection(p.splitlines())
        if horiz_reflection is not None:
            reflections.append((horiz_reflection + 1) * 100)

    print(sum(reflections))


if __name__ == "__main__":
    main()
