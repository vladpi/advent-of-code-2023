import re


def calc_card_points(card: str) -> int:
    card_id, win, my = re.match(r"Card\s+(\d+): (.+)\s\|\s(.*)", card).groups()
    win = set(map(int, win.split()))
    my = set(map(int, my.split()))
    my_wins = len(win.intersection(my))
    if my_wins == 0:
        return 0
    return 2**(my_wins-1)


def main():
    with open("input.txt", "r") as file:
        data = file.read().splitlines()

    res = 0
    for card in data:
        res += calc_card_points(card)
    print(res)


if __name__ == "__main__":
    main()
