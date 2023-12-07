class Hand:
    def __init__(self, v: str) -> None:
        cards, bid = v.split()
        self.cards: list[str] = list(cards)
        self.cards_number: list[str] = cards_to_numbers(self.cards)
        self.bid: int = int(bid)
        self.power = calc_cards_power(self.cards)

    def __lt__(self, other: "Hand") -> bool:
        if self.power == other.power:
            return self.cards_number < other.cards_number
        return self.power < other.power


def cards_to_numbers(cards: list[str]) -> list[int]:
    card_to_number = {
        card: number
        for number, card in enumerate(
            reversed(["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]),
        )
    }

    return [card_to_number[c] for c in cards]


def calc_cards_power(cards: list[str]) -> int:
    power_by_config = {
        (1, 5): 7,
        (2, 4): 6,
        (2, 3): 5,
        (3, 3): 4,
        (3, 2): 3,
        (4, 2): 2,
        (5, 1): 1,
    }

    cards_count = {}
    for card in cards:
        cards_count.setdefault(card, 0)
        cards_count[card] += 1

    j_count = cards_count.pop("J", 0)
    if len(cards_count) == 0:
        return 7

    return power_by_config[len(cards_count), max(cards_count.values()) + j_count]


def main():
    with open("input.txt", "r") as file:
        data = file.read()

    result = 0
    hands = sorted([Hand(l) for l in data.splitlines()])
    for rank, hand in enumerate(hands, start=1):
        result += rank * hand.bid
    print(result)


if __name__ == "__main__":
    main()
