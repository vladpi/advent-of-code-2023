from itertools import pairwise


def get_diff(v: list[int]) -> list[int]:
    return [y - x for (x, y) in pairwise(v)]


def main():
    with open("input.txt", "r") as file:
        data = file.read()

    result = 0
    for history in data.splitlines():
        history = list(map(int, history.split()))

        next_el = history[-1]
        last_diff = get_diff(history)
        while last_diff:
            next_el += last_diff[-1]
            last_diff = get_diff(last_diff)

        result += next_el

    print(result)


if __name__ == "__main__":
    main()
