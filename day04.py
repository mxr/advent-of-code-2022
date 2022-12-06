from __future__ import annotations

import functools
from collections.abc import Generator


@functools.cache
def parse(filename: str) -> tuple[tuple[int, int, int, int], ...]:
    def gen() -> Generator[tuple[int, int, int, int], None, None]:
        with open(filename) as f:
            for rp in f.readlines():
                rp1, _, rp2 = rp.partition(",")
                r1, _, r2 = rp1.partition("-")
                r3, _, r4 = rp2.partition("-")

                yield int(r1), int(r2), int(r3), int(r4)

    return tuple(gen())


def part1(filename: str) -> int:
    return sum(
        n1 <= n3 <= n4 <= n2 or n3 <= n1 <= n2 <= n4
        for n1, n2, n3, n4 in parse(filename)
    )


def part2(filename: str) -> int:
    return sum(n1 <= n3 <= n2 or n3 <= n1 <= n4 for n1, n2, n3, n4 in parse(filename))


if __name__ == "__main__":
    from _common import main

    raise SystemExit(main(part1, part2))
