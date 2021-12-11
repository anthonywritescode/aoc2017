from __future__ import annotations

import argparse
import os.path

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def _hash(s: str) -> int:
    """from day 10 part 2"""
    size = 256
    numbers = list(range(size))

    lengths = [ord(c) for c in s.strip()] + [17, 31, 73, 47, 23]

    i = 0
    skip = 0

    for _ in range(64):
        for length in lengths:
            if i + length <= size:
                slc = numbers[i:i + length]
                slc.reverse()
                numbers[i:i + length] = slc
            else:
                slc = numbers[i:] + numbers[:length - (size - i)]
                slc.reverse()
                numbers[i:] = slc[:size - i]
                numbers[:length - (size - i)] = slc[size - i:]

            i += length + skip
            i %= size
            skip += 1

    def hashes(nums: list[int]) -> int:
        base = nums[0]
        for num in nums[1:]:
            base ^= num
        return base

    dense = [hashes(numbers[i * 16:i * 16 + 16]) for i in range(16)]
    return int(''.join(f'{num:02x}' for num in dense), 16)


def compute(s: str) -> int:
    s = s.strip()
    total = 0
    for i in range(128):
        total += bin(_hash(f'{s}-{i}')).count('1')
    return total


INPUT_S = '''\
flqrgnkx
'''
EXPECTED = 8108


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
