from functools import reduce
from itertools import pairwise


def get_diff(v: list[int]) -> list[int]:
    return [y - x for (x, y) in pairwise(v)]


def main():
    with open("input.txt", "r") as file:
        data = file.read()

    result = 0
    for history in data.splitlines():
        history = list(map(int, history.split()))

        first_els = [history[0]]
        last_diff = get_diff(history)
        while last_diff:
            first_els.append(last_diff[0])
            last_diff = get_diff(last_diff)

        result += reduce(lambda x, y: y - x, reversed(first_els))

    print(result)


if __name__ == "__main__":
    main()
