from __future__ import annotations

import argparse
import os.path

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    target = int(s)

    i = 0
    while (1 + i * 2) * (1 + i * 2) < target:
        i += 1

    corners = [
        (1 + i * 2) * (1 + i * 2) - 2 * i * n
        for n in range(4)
    ]

    min_dist = min(abs(corner - target) for corner in corners)

    return 2 * i - min_dist


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        ('1', 0),
        ('12', 3),
        ('23', 2),
        ('1024', 31),
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
