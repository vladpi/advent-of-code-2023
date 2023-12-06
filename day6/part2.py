def main():
    with open("input.txt", "r") as file:
        data = file.read()

    time_str, distance_str = data.splitlines()
    time = int("".join(time_str.split()[1:]))
    distance = int("".join(distance_str.split()[1:]))

    wins_count = 0
    for hold_time in range(1, time):
        if hold_time*(time-hold_time) > distance:
            wins_count += 1
    print(wins_count)


if __name__ == "__main__":
    main()
