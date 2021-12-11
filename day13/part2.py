from __future__ import annotations

import argparse
import os.path

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    nums = []
    for line in s.splitlines():
        a, b = line.split(': ')
        nums.append((int(a), int(b)))

    i = 1
    while True:
        if all(
            (i + a) % ((b - 1) * 2) != 0
            for a, b in nums
        ):
            return i
        i += 1

    raise AssertionError('unreachable')


INPUT_S = '''\
0: 3
1: 2
4: 4
6: 4
'''
EXPECTED = 10


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

    with open(args.data_file) as f, timing('brute force'):
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
