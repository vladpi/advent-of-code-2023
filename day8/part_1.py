import re
from itertools import cycle


class Node:
    def __init__(self, v: str) -> None:
        name, left, right = re.match(r"([A-Z]+) = \(([A-Z]+), ([A-Z]+)\)", v).groups()
        self.name = name
        self.left = left
        self.right = right

    def next(self, instruction: str) -> str | None:
        if instruction == "L":
            return self.left
        elif instruction == "R":
            return self.right


def main():
    with open("input.txt", "r") as file:
        data = file.read()

    instructions, _, *raw_nodes = data.splitlines()
    print(instructions)
    print(raw_nodes)

    nodes = {}
    for n in raw_nodes:
        node = Node(n)
        nodes[node.name] = node

    steps = 0
    curr_node = "AAA"
    for i in cycle(instructions):
        if curr_node == "ZZZ":
            break

        curr_node = nodes[curr_node].next(i)
        steps += 1

    print(steps)


if __name__ == "__main__":
    main()
