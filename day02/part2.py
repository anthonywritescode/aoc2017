from __future__ import annotations

import argparse
import os.path

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    total = 0

    lines = s.splitlines()
    for line in lines:
        nums = [int(s) for s in line.split()]
        for i, num in enumerate(nums):
            for other in nums[i + 1:]:
                if max(other, num) % min(other, num) == 0:
                    total += max(other, num) // min(other, num)
                    break
    return total


INPUT_S = '''\
5 9 2 8
9 4 7 3
3 8 6 5
'''
EXPECTED = 9


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
