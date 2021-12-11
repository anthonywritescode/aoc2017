from __future__ import annotations

import argparse
import os.path

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    s = s.strip()

    total = 0

    half = len(s) // 2
    for i, c in enumerate(s):
        if s[(i + half) % len(s)] == c:
            total += int(c)

    return total


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        ('1212', 6),
        ('1221', 0),
        ('123123', 12),
        ('12131415', 4),
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
