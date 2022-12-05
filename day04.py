from __future__ import annotations

import functools
from collections.abc import Generator


def parse(filename: str) -> str:
    with open(filename) as f:
        return f.read()


@functools.cache
def helper(filename: str) -> tuple[tuple[int, int, int, int], ...]:
    def gen() -> Generator[tuple[int, int, int, int], None, None]:
        for rp in parse(filename).splitlines():
            rp1, _, rp2 = rp.partition(",")
            r1, _, r2 = rp1.partition("-")
            r3, _, r4 = rp2.partition("-")

            yield int(r1), int(r2), int(r3), int(r4)

    return tuple(gen())


def part1(filename: str) -> int:
    return sum(
        n1 <= n3 <= n4 <= n2 or n3 <= n1 <= n2 <= n4
        for n1, n2, n3, n4 in helper(filename)
    )


def part2(filename: str) -> int:
    return sum(n1 <= n3 <= n2 or n3 <= n1 <= n4 for n1, n2, n3, n4 in helper(filename))


if __name__ == "__main__":
    from _common import main

    raise SystemExit(main(part1, part2))
