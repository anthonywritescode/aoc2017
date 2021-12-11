from __future__ import annotations

import argparse
import os.path

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

A_FACTOR = 16807
B_FACTOR = 48271
DIV = 2147483647


def compute(s: str) -> int:
    _, _, _, _, initial_a_s, _, _, _, _, initial_b_s = s.split()

    count = 0
    a = int(initial_a_s)
    b = int(initial_b_s)
    for i in range(5_000_000):
        a = a * A_FACTOR % DIV
        while a % 4 != 0:
            a = a * A_FACTOR % DIV

        b = b * B_FACTOR % DIV
        while b % 8 != 0:
            b = b * B_FACTOR % DIV

        if a % 2 ** 16 == b % 2 ** 16:
            count += 1

    return count


INPUT_S = '''\
Generator A starts with 65
Generator B starts with 8921
'''
EXPECTED = 309


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
