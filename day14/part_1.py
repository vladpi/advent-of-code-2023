def main():
    with open("input.txt", "r") as file:
        data = file.read().splitlines()

    for idx, row in enumerate(data):
        data[idx] = list(row)

    for j in range(len(data[0])):
        empty_cells = []

        for i in range(len(data)):
            if data[i][j] == ".":
                empty_cells.append(i)
            if data[i][j] == "#":
                empty_cells = []
            if data[i][j] == "O" and empty_cells:
                new_i = min(empty_cells)
                data[i][j] = "."
                data[new_i][j] = "O"
                empty_cells.remove(new_i)
                empty_cells.append(i)

    result = 0
    for idx, row in enumerate(data):
        result += row.count("O") * (len(data) - idx)

    print(result)


if __name__ == "__main__":
    main()
