from __future__ import annotations

import argparse
import collections
import os.path

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    registers: dict[str, int] = collections.defaultdict(int)

    def val(op: str) -> int:
        if op.isalpha():
            return registers[op]
        else:
            return int(op)

    pc = 0
    instructions = [line.split() for line in s.splitlines()]
    mul = 0
    while True:
        try:
            parts = instructions[pc]
        except IndexError:
            break
        if parts[0] == 'set':
            registers[parts[1]] = val(parts[2])
        elif parts[0] == 'sub':
            registers[parts[1]] -= val(parts[2])
        elif parts[0] == 'mul':
            registers[parts[1]] *= val(parts[2])
            mul += 1
        elif parts[0] == 'jnz':
            if val(parts[1]) != 0:
                pc += val(parts[2])
            else:
                pc += 1
            continue

        pc += 1

    return mul


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
