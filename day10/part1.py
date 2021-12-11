from __future__ import annotations

import argparse
import os.path

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str, *, size: int = 256) -> int:
    numbers = list(range(size))

    i = 0
    skip = 0
    lengths = [int(part) for part in s.strip().split(',')]

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

    return numbers[0] * numbers[1]


INPUT_S = '''\
3,4,1,5
'''
EXPECTED = 12


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, EXPECTED),
    ),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s, size=5) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f, timing():
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
