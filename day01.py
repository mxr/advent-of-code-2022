from __future__ import annotations

import functools


def parse(filename: str) -> str:
    with open(filename) as f:
        return f.read()


@functools.cache
def helper(filename: str) -> list[int]:
    return [
        sum(int(cal) for cal in elf.splitlines())
        for elf in parse(filename).split("\n\n")
    ]


def part1(filename: str) -> int:
    return max(helper(filename))


def part2(filename: str) -> int:
    return sum(sorted(helper(filename), reverse=True)[:3])


if __name__ == "__main__":
    from _common import main

    raise SystemExit(main(part1, part2))
