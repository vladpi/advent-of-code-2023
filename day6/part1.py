def main():
    with open("input.txt", "r") as file:
        data = file.read()

    time_str, distance_str = data.splitlines()
    times = map(int, time_str.split()[1:])
    distances = map(int, distance_str.split()[1:])

    result = 1
    for t, d in zip(times, distances):
        wins_count = 0
        for hold_time in range(1, t):
            if hold_time*(t-hold_time) > d:
                wins_count += 1
        result *= wins_count
    print(result)


if __name__ == "__main__":
    main()
