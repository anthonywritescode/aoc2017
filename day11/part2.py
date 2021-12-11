from __future__ import annotations

import argparse
import os.path

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

DIRS = {
    'n': (0, 2),
    's': (0, -2),
    'ne': (1, 1),
    'se': (1, -1),
    'nw': (-1, 1),
    'sw': (-1, -1),
}


def dist(x: int, y: int) -> int:
    x = abs(x)
    y = abs(y)

    if x > y:
        return x
    else:
        return x + (y - x) // 2


def compute(s: str) -> int:
    x = y = max_dist = 0
    for part in s.strip().split(','):
        d_x, d_y = DIRS[part]
        x, y = x + d_x, y + d_y
        max_dist = max(max_dist, dist(x, y))

    return max_dist


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (),
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
