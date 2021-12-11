from __future__ import annotations

import argparse
import os.path

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    numbers = [int(line) for line in s.split()]

    seen = {tuple(numbers)}
    n = 0
    while True:
        m = max(numbers)
        i = numbers.index(m)
        numbers[i] = 0
        for j in range(m):
            numbers[(i + 1 + j) % len(numbers)] += 1

        n += 1
        key = tuple(numbers)
        if key in seen:
            return n
        else:
            seen.add(key)

    raise AssertionError('unreachable')


INPUT_S = '''\
0 2 7 0
'''
EXPECTED = 5


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
