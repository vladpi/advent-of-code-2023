def holiday_hash(v: str) -> int:
    current_value = 0
    for c in v:
        current_value += ord(c)
        current_value *= 17
        current_value %= 256
    return current_value


def main():
    with open("input.txt", "r") as file:
        data = file.read()

    hashes = []
    for instruction in data.split(","):
        hashes.append(holiday_hash(instruction))

    print(sum(hashes))


if __name__ == "__main__":
    main()
