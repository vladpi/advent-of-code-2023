from dataclasses import dataclass


@dataclass
class MapItem:
    destination_range_start: int
    source_range_start: int
    range_len: int


@dataclass
class Map:
    name: str
    items: list[MapItem]

    def map(self, source: int) -> int:
        for i in self.items:
            if i.source_range_start <= source < i.source_range_start + i.range_len:
                return i.destination_range_start + (source - i.source_range_start)
        return source


def parse_map(m: str) -> Map:
    map_strings = m.splitlines()
    return Map(
        name=map_strings[0].split()[0],
        items=[MapItem(*map(int, v.split(" "))) for v in map_strings[1:]],
    )


def main():
    with open("input.txt", "r") as file:
        data = file.read()

    data = data.split("\n\n")

    seeds = map(int, data[0].split()[1:])
    maps = [parse_map(d) for d in data[1:]]

    locations = []
    for seed in seeds:
        mapped = seed
        for m in maps:
            mapped = m.map(mapped)
        locations.append(mapped)

    print(min(locations))


if __name__ == "__main__":
    main()
