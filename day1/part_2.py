WORD_TO_DIGIT = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def find_line_number(v: str) -> int:
    digits_indexes = {}
    for digit in map(str, range(0, 10)):
        try:
            digits_indexes[v.index(digit)] = digit
            digits_indexes[v.rindex(digit)] = digit
        except ValueError:
            pass

    for digit_word, digit in WORD_TO_DIGIT.items():
        try:
            digits_indexes[v.index(digit_word)] = digit
            digits_indexes[v.rindex(digit_word)] = digit
        except ValueError:
            pass

    first_digit = digits_indexes[min(digits_indexes.keys())]
    last_digit = digits_indexes[max(digits_indexes.keys())]

    return int(first_digit + last_digit)


def main():
    with open("input.txt", "r") as file:
        data = file.read()

    result = 0
    for line in data.split("\n"):
        result += find_line_number(line)

    print(result)


if __name__ == "__main__":
    main()
