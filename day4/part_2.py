import re


def calc_card_points(card: str) -> tuple[int, int]:
    card_id, win, my = re.match(r"Card\s+(\d+): (.+)\s\|\s(.*)", card).groups()
    win = set(map(int, win.split()))
    my = set(map(int, my.split()))
    my_wins = len(win.intersection(my))
    if my_wins == 0:
        return 0, 0
    return my_wins, 2 ** (my_wins - 1)


def main():
    with open("input.txt", "r") as file:
        data = file.read().splitlines()

    cards_repeats = [1 for _ in range(len(data))]
    for idx, card in enumerate(data):
        wins, _ = calc_card_points(card)
        for i in range(wins):
            cards_repeats[idx + i + 1] += cards_repeats[idx]

    print(sum(cards_repeats))


if __name__ == "__main__":
    main()
