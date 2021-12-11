from __future__ import annotations

import argparse
import contextlib
import os.path

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

DIRECTIONS = {
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
}


def compute(s: str) -> str:
    grid = s.splitlines()
    x, = (i for i, c in enumerate(grid[0]) if c == '|')
    y = 0
    d_y, d_x = 1, 0

    seen = ''
    while True:
        y, x = y + d_y, x + d_x
        if grid[y][x] == '+':
            for c_d_y, c_d_x in DIRECTIONS - {(-1 * d_y, -1 * d_x)}:
                with contextlib.suppress(IndexError):
                    if grid[y + c_d_y][x + c_d_x] != ' ':
                        d_y, d_x = c_d_y, c_d_x
                        break
            else:
                raise AssertionError('unreachable')
        elif grid[y][x].isalpha():
            seen += grid[y][x]
        elif grid[y][x] == ' ':
            break
    return seen


INPUT_S = '''\
     |
     |  +--+
     A  |  C
 F---|----E|--+
     |  |  |  D
     +B-+  +--+
'''
EXPECTED = 'ABCDEF'


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, EXPECTED),
    ),
)
def test(input_s: str, expected: str) -> None:
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
