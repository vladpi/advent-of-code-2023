import math
from collections import defaultdict
from dataclasses import dataclass, field
from enum import Enum
from typing import Protocol


class Impulse(Enum):
    LOW = "LOW"
    HIGH = "HIGH"


class Module(Protocol):
    name: str
    output_modules: list[str]

    def handle_impulse(self, source: str, impulse: Impulse) -> Impulse | None:
        ...


@dataclass
class FlipFlop:
    name: str
    output_modules: list[str]

    is_on: bool = False

    def handle_impulse(self, source: str, impulse: Impulse) -> Impulse | None:
        if impulse == Impulse.HIGH:
            return None

        self.is_on = not self.is_on
        if self.is_on:
            return Impulse.HIGH
        else:
            return Impulse.LOW

    def __repr__(self) -> str:
        return f"<{self.name} {self.is_on=} {self.output_modules=}>"


@dataclass
class Conjunction:
    name: str
    output_modules: list[str]

    input_modules_states: dict[str, Impulse] = field(default_factory=dict)

    def set_input_modules(self, input_modules: list[str]):
        for input_module in input_modules:
            self.input_modules_states[input_module] = Impulse.LOW

    def handle_impulse(self, source: str, impulse: Impulse) -> Impulse | None:
        self.input_modules_states[source] = impulse

        if all(i == Impulse.HIGH for i in self.input_modules_states.values()):
            return Impulse.LOW
        else:
            return Impulse.HIGH

    def __repr__(self) -> str:
        return f"<{self.name} {self.output_modules=} {self.input_modules_states=}>"


@dataclass
class Broadcast:
    name: str
    output_modules: list[str]

    def handle_impulse(self, source: str, impulse: Impulse) -> Impulse | None:
        return impulse

    def __repr__(self) -> str:
        return f"<{self.name} {self.output_modules=}>"


def parse_module(module_str: str) -> Module:
    if module_str.startswith("%"):
        module_cls = FlipFlop
        module_str = module_str.removeprefix("%")

    elif module_str.startswith("&"):
        module_cls = Conjunction
        module_str = module_str.removeprefix("&")

    elif module_str.startswith("broadcaster"):
        module_cls = Broadcast

    name, outputs_str = module_str.split(" -> ")
    outputs = outputs_str.split(", ")

    return module_cls(name=name, output_modules=outputs)


def init_input_modules_for_conjunctions(modules: list[Module]):
    all_input_modules = defaultdict(list)

    for module in modules:
        for output in module.output_modules:
            all_input_modules[output].append(module.name)

    for module in modules:
        if isinstance(module, Conjunction):
            module.set_input_modules(all_input_modules.get(module.name, []))


def push_button(modules_map: dict[str, Module], rx_input: Module) -> list[str]:
    low_count = 1
    hight_count = 0

    impulses_queue = [("button", "broadcaster", Impulse.LOW)]

    triggered_rx_input_inputs = []

    while impulses_queue:
        source_module, target_module, impulse = impulses_queue.pop(0)
        module = modules_map.get(target_module)
        if module is None:
            continue

        new_impulse = module.handle_impulse(source_module, impulse)
        if new_impulse is None:
            continue

        if target_module == rx_input.name and impulse == Impulse.HIGH:
            triggered_rx_input_inputs.append(source_module)

        if new_impulse == Impulse.LOW:
            low_count += len(module.output_modules)
        else:
            hight_count += len(module.output_modules)

        for output_module in module.output_modules:
            impulses_queue.append((module.name, output_module, new_impulse))

    return triggered_rx_input_inputs


def main():
    with open("input.txt", "r") as file:
        data = file.read()

    modules = []
    for module_str in data.splitlines():
        modules.append(parse_module(module_str))
    init_input_modules_for_conjunctions(modules)

    modules_map = {m.name: m for m in modules}

    rx_input = [m for m in modules if "rx" in m.output_modules][0]
    targets_button_pushes = {
        output: None for output in rx_input.input_modules_states.keys()
    }

    pushes_count = 0
    while not all(targets_button_pushes.values()):
        pushes_count += 1

        triggered_rx_input_inputs = push_button(modules_map, rx_input)
        for rx_input_input in triggered_rx_input_inputs:
            if targets_button_pushes[rx_input_input] is None:
                targets_button_pushes[rx_input_input] = pushes_count

    print(math.lcm(*targets_button_pushes.values()))


if __name__ == "__main__":
    main()
