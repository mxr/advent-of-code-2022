from __future__ import annotations


def parse(filename: str) -> str:
    with open(filename) as f:
        return f.read()


def part1(filename: str) -> int:
    common = []
    for rucksack in parse(filename).splitlines():
        middle = len(rucksack) // 2
        partition1, partition2 = (rucksack[:middle], rucksack[middle:])
        common.append((set(partition1) & set(partition2)).pop())

    return sum(ord(c) - (96 if "a" <= c <= "z" else 38) for c in common)


def part2(filename: str) -> int:
    common = []

    i = 0
    rucksacks = parse(filename).splitlines()
    while i < len(rucksacks):
        r1, r2, r3 = rucksacks[i], rucksacks[i + 1], rucksacks[i + 2]
        common.append((set(r1) & set(r2) & set(r3)).pop())
        i += 3

    return sum(ord(c) - (96 if "a" <= c <= "z" else 38) for c in common)


if __name__ == "__main__":
    from _common import main

    raise SystemExit(main(part1, part2))
