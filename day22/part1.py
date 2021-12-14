from __future__ import annotations

import argparse
import os.path

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

DIRECTIONS = (
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0),
)


def compute(s: str) -> int:
    coords = set()
    for y, line in enumerate(s.splitlines()):
        for x, c in enumerate(line):
            if c == '#':
                coords.add((x, y))

    pos = (len(line) // 2, len(line) // 2)
    direction = DIRECTIONS[0]

    infections = 0
    for _ in range(10000):
        if pos in coords:
            direction = DIRECTIONS[(DIRECTIONS.index(direction) + 1) % 4]
            coords.discard(pos)
        else:
            direction = DIRECTIONS[(DIRECTIONS.index(direction) - 1) % 4]
            coords.add(pos)
            infections += 1

        pos = (pos[0] + direction[0], pos[1] + direction[1])

    return infections


INPUT_S = '''\
..#
#..
...
'''
EXPECTED = 5587


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, EXPECTED),
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
