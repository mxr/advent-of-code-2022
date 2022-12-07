from __future__ import annotations

import functools


@functools.cache
def parse(filename: str) -> tuple[int, ...]:
    with open(filename) as f:
        return tuple(
            sum(int(line) for line in chunk.splitlines())
            for chunk in f.read().split("\n\n")
        )


def part1(filename: str) -> int:
    return max(parse(filename))


def part2(filename: str) -> int:
    return sum(sorted(parse(filename), reverse=True)[:3])


if __name__ == "__main__":
    from _common import main

    raise SystemExit(main(part1, part2))
