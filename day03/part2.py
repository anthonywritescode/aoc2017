from __future__ import annotations

import argparse
import os.path
from typing import Generator

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def adjacent(x: int, y: int) -> Generator[tuple[int, int], None, None]:
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            if i == j == 0:
                continue
            else:
                yield x + i, y + j


DIRECTIONS = (
    (0, -1),
    (-1, 0),
    (0, 1),
    (1, 0),
)


def compute(s: str) -> int:
    target = int(s)

    direction = DIRECTIONS[2]
    x = y = 0
    coords = {}
    coords[x, y] = val = 1

    while val <= target:
        next_dir = DIRECTIONS[(DIRECTIONS.index(direction) + 1) % 4]
        if (x + next_dir[0], y + next_dir[1]) not in coords:
            direction = next_dir

        x, y = x + direction[0], y + direction[1]
        val = 0
        for coord in adjacent(x, y):
            val += coords.get(coord, 0)
        coords[(x, y)] = val

    return val


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        ('55', 57),
        ('3', 4),
        ('24', 25),
        ('25', 26),
    ),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f, timing():
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
