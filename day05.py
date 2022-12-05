from __future__ import annotations

import re
from itertools import zip_longest

RE = re.compile(r"\d+")
SKIP = frozenset(("[", "]", " "))


def parse(filename: str) -> str:
    with open(filename) as f:
        return f.read()


def part1(filename: str) -> int:
    positions, instructions = parse(filename).split("\n\n")

    cols = tuple(
        zip_longest(*tuple(tuple(s) for s in positions.splitlines()), fillvalue=" ")
    )

    i = 1
    stacks = []
    while i < len(cols):
        col = cols[i]
        stacks.append(
            [col[i] for i in range(len(col) - 2, -1, -1) if col[i] not in SKIP]
        )
        i += 4

    for instr in instructions.splitlines():
        nums = RE.findall(instr)
        assert nums, instr
        amt, s1, s2 = int(nums[0]), int(nums[1]) - 1, int(nums[2]) - 1

        for _ in range(amt):
            stacks[s2].append(stacks[s1].pop())

    print("".join(s[-1] for s in stacks), end=" ")
    return -1


def part2(filename: str) -> int:
    positions, instructions = parse(filename).split("\n\n")

    cols = tuple(
        zip_longest(*tuple(tuple(s) for s in positions.splitlines()), fillvalue=" ")
    )

    i = 1
    stacks = []
    while i < len(cols):
        col = cols[i]
        stacks.append(
            [col[i] for i in range(len(col) - 2, -1, -1) if col[i] not in SKIP]
        )
        i += 4

    for instr in instructions.splitlines():
        nums = RE.findall(instr)
        assert nums, instr
        amt, s1, s2 = int(nums[0]), int(nums[1]) - 1, int(nums[2]) - 1

        tmp = []
        for _ in range(amt):
            tmp.append(stacks[s1].pop())
        stacks[s2].extend(reversed(tmp))

    print("".join(s[-1] for s in stacks), end=" ")
    return -1


if __name__ == "__main__":
    from _common import main

    raise SystemExit(main(part1, part2))
