from __future__ import annotations

import argparse
import math
import os.path

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def is_prime(n: int) -> bool:
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    else:
        return True


def compute(s: str) -> int:
    # determined by reverse-engineering the code
    c = 0
    n = 108100
    while True:
        if not is_prime(n):
            c += 1
        if n == 125100:
            break
        n += 17

    return c


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (),
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
