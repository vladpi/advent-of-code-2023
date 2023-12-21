import re
from typing import NamedTuple

ACCEPT = "A"
REJECT = "R"


class Instruction(NamedTuple):
    condition: str | None
    target: str


def parse_workflow_step(step: str) -> tuple[str, list[Instruction]]:
    name, instructions_str = re.match(r"(.+)\{(.+?)\}", step).groups()

    instructions = []
    instructions_strs = instructions_str.split(",")
    for instruction_str in instructions_strs[:-1]:
        instructions.append(Instruction(*instruction_str.split(":")))
    instructions.append(Instruction(condition=None, target=instructions_strs[-1]))

    return name, instructions


def check_part(workflow_map: dict[str, list[Instruction]], part: str) -> bool:
    exec(part.replace(",", ";")[1:-1])

    workflow = "in"

    while True:
        if workflow == "A":
            return True
        if workflow == "R":
            return False

        instructions = workflow_map[workflow]
        for i in instructions:
            if i.condition is None or eval(i.condition):
                workflow = i.target
                break


def get_rating(part: str) -> int:
    exec(part.replace(",", ";")[1:-1])
    return eval("x+m+a+s")


def main():
    with open("input.txt", "r") as file:
        data = file.read()

    workflows_str, parts_str = data.split("\n\n")

    workflow_map = {}
    for step_str in workflows_str.splitlines():
        name, instructions = parse_workflow_step(step_str)
        workflow_map[name] = instructions

    accepted_ratings = []
    for part_str in parts_str.splitlines():
        if check_part(workflow_map, part_str):
            accepted_ratings.append(get_rating(part_str))
    print(sum(accepted_ratings))


if __name__ == "__main__":
    main()
