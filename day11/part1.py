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


def compute(s: str) -> int:
    x = y = 0
    for part in s.strip().split(','):
        d_x, d_y = DIRS[part]
        x, y = x + d_x, y + d_y

    x = abs(x)
    y = abs(y)

    if x > y:
        return x
    else:
        return x + (y - x) // 2


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        ('ne,se,ne,se', 4),
        ('ne,ne,ne', 3),
        ('nw,nw,nw', 3),
        ('n,n,n', 3),
        ('s,s,s', 3),
        ('se,se,se', 3),
        ('sw,sw,sw', 3),
        ('ne,ne,sw,sw', 0),
        ('ne,ne,s,s', 2),
        ('se,sw,se,sw,sw', 3),
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
