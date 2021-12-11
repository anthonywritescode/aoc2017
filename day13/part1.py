from __future__ import annotations

import argparse
import os.path

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    depths = {}
    for line in s.splitlines():
        k_s, v_s = line.split(': ')
        depths[int(k_s)] = int(v_s)

    positions = {k: 0 for k in depths}
    directions = {k: 1 for k in depths}

    total = 0
    for i in range(max(positions) + 1):
        if i in positions and positions[i] == 0:
            total += i * depths[i]

        for k, v in positions.items():
            if directions[k] == -1 and v == 0:
                directions[k] = 1
                positions[k] = 1
            elif directions[k] == 1 and v == depths[k] - 1:
                directions[k] = -1
                positions[k] = depths[k] - 2
            else:
                positions[k] += directions[k]

    return total


INPUT_S = '''\
0: 3
1: 2
4: 4
6: 4
'''
EXPECTED = 24


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
