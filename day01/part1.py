from __future__ import annotations

import argparse
import os.path

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    s = s.strip()

    total = 0
    # special case last digit
    if s[-1] == s[0]:
        total += int(s[-1])

    for i, c in enumerate(s[:-1]):
        if s[i + 1] == c:
            total += int(c)

    return total


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        ('1122', 3),
        ('1111', 4),
        ('1234', 0),
        ('91212129', 9),
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
