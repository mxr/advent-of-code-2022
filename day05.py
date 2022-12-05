from __future__ import annotations

import functools
import re
from itertools import zip_longest

RE = re.compile(r"\d+")
SKIP = frozenset(("[", "]", " "))


def parse(filename: str) -> str:
    with open(filename) as f:
        return f.read()


@functools.cache
def helper(filename: str) -> tuple[list[tuple[str, ...]], list[tuple[int, int, int]]]:
    positions, instructions = parse(filename).split("\n\n")

    cols = tuple(
        zip_longest(*tuple(tuple(s) for s in positions.splitlines()), fillvalue=" ")
    )

    i = 1
    initial_stacks = []
    while i < len(cols):
        col = cols[i]
        initial_stacks.append(
            tuple(col[i] for i in range(len(col) - 2, -1, -1) if col[i] not in SKIP)
        )
        i += 4

    nums = []
    for instr in instructions.splitlines():
        raw_nums = RE.findall(instr)
        assert raw_nums, instr

        amt, s1, s2 = int(raw_nums[0]), int(raw_nums[1]) - 1, int(raw_nums[2]) - 1
        nums.append((amt, s1, s2))

    return initial_stacks, nums


def part1(filename: str) -> int:
    initial_stacks, nums = helper(filename)
    stacks = [list(s) for s in initial_stacks]

    for amt, s1, s2 in nums:
        stacks[s1], top = stacks[s1][:-amt], reversed(stacks[s1][-amt:])
        stacks[s2].extend(top)

    print("".join(s[-1] for s in stacks), end=" ")
    return -1


def part2(filename: str) -> int:
    initial_stacks, nums = helper(filename)
    stacks = [list(s) for s in initial_stacks]

    for amt, s1, s2 in nums:
        stacks[s1], top = stacks[s1][:-amt], stacks[s1][-amt:]
        stacks[s2].extend(top)

    print("".join(s[-1] for s in stacks), end=" ")
    return -1


if __name__ == "__main__":
    from _common import main

    raise SystemExit(main(part1, part2))
