import re

BALLS_PER_GAME = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def calc_game_min_configuration(rounds: list[str]) -> dict[str, int]:
    config = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }

    for r in rounds:
        parsed_round = parse_round(r)
        for color, num in parsed_round.items():
            if config[color] < num:
                config[color] = num

    return config


def parse_game(game_line: str) -> tuple[int, list[str]]:
    game_match = re.match(r"Game (\d+):", game_line)
    game_id = int(game_match.groups()[0])

    rounds = game_line.replace(game_match.group(), "").split(";")

    return game_id, rounds


def parse_round(round: str) -> dict[str, int]:
    parsed_round = {}
    for m in re.findall(r"((\d+) (blue|red|green))", round):
        _, num, color = m
        parsed_round[color] = int(num)
    return parsed_round


def main():
    with open("input.txt", "r") as file:
        data = file.read()

    games_powers = []
    for game in data.split("\n"):
        game_id, rounds = parse_game(game)
        config = calc_game_min_configuration(rounds)
        power = config["red"] * config["blue"] * config["green"]
        games_powers.append(power)

    print(sum(games_powers))


if __name__ == "__main__":
    main()
