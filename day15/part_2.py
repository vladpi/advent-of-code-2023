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

    boxes = {}
    for instruction in data.split(","):
        if instruction.endswith("-"):
            label = instruction[:-1]
            label_hash = holiday_hash(label)
            boxes.get(label_hash, {}).pop(label, None)

        else:
            label, focal_length = instruction.split("=")
            label_hash = holiday_hash(label)
            focal_length = int(focal_length)

            boxes.setdefault(label_hash, {})
            boxes[label_hash][label] = focal_length

    focusing_powers = []
    for box, content in boxes.items():
        for idx, focal_length in enumerate(content.values(), start=1):
            focusing_powers.append((box + 1) * idx * focal_length)

    print(sum(focusing_powers))


if __name__ == "__main__":
    main()
