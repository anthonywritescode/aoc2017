from __future__ import annotations

import argparse
import os.path

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> str:
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
    return ''.join(f'{num:02x}' for num in dense)


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        ('', 'a2582a3a0e66e6e86e3812dcb672a272'),
        ('AoC 2017', '33efeb34ea91902bb2f59c9920caa6cd'),
        ('1,2,3', '3efbe78a8d82f29979031a4aa0b16a9d'),
        ('1,2,4', '63960835bcdc130f0b66d7ff4f6a5a8e'),
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
