import re

BALLS_PER_GAME = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def is_valid_game(rounds: list[str]) -> bool:
    for r in rounds:
        if not is_valid_round(r):
            return False
    return True


def parse_game(game_line: str) -> tuple[int, list[str]]:
    game_match = re.match(r"Game (\d+):", game_line)
    game_id = int(game_match.groups()[0])

    rounds = game_line.replace(game_match.group(), "").split(";")

    return game_id, rounds


def is_valid_round(round: str) -> bool:
    for m in re.findall(r"((\d+) (blue|red|green))", round):
        _, num, color = m
        if int(num) > BALLS_PER_GAME[color]:
            return False
    return True


def main():
    with open("02_input.txt", "r") as file:
        data = file.read()

    valid_games = []
    for game in data.split("\n"):
        game_id, rounds = parse_game(game)
        if is_valid_game(rounds):
            valid_games.append(game_id)

    print(sum(valid_games))


if __name__ == "__main__":
    main()
