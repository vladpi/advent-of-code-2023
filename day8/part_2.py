import math
import re
from itertools import cycle


class Node:
    def __init__(self, v: str) -> None:
        name, left, right = re.match(r"(.+) = \((.+), (.+)\)", v).groups()
        self.name = name
        self.left = left
        self.right = right

    def next(self, instruction: str) -> str | None:
        if instruction == "L":
            return self.left
        elif instruction == "R":
            return self.right


def calc_steps(nodes: dict[str, Node], start_node: str, instructions: str) -> int:
    steps = 0
    curr_node = start_node
    for i in cycle(instructions):
        if curr_node.endswith("Z"):
            break

        curr_node = nodes[curr_node].next(i)
        steps += 1

    return steps


def main():
    with open("input.txt", "r") as file:
        data = file.read()

    instructions, _, *raw_nodes = data.splitlines()

    nodes = {}
    for n in raw_nodes:
        node = Node(n)
        nodes[node.name] = node

    curr_nodes = [n for n in nodes.keys() if n.endswith("A")]
    steps = []
    for n in curr_nodes:
        steps.append(calc_steps(nodes, n, instructions))
    result = math.lcm(*steps)

    print(result)


if __name__ == "__main__":
    main()
