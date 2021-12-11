from __future__ import annotations

import argparse
import collections
import os.path

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    registers: dict[str, int] = collections.defaultdict(int)
    prog = [line.split() for line in s.splitlines()]

    def val(op: str) -> int:
        if op.isalpha():
            return registers[op]
        else:
            return int(op)

    played = None
    pc = 0
    while True:
        instruction = prog[pc]
        if instruction[0] == 'snd':
            played = val(instruction[1])
        elif instruction[0] == 'set':
            registers[instruction[1]] = val(instruction[2])
        elif instruction[0] == 'add':
            registers[instruction[1]] += val(instruction[2])
        elif instruction[0] == 'mul':
            registers[instruction[1]] *= val(instruction[2])
        elif instruction[0] == 'mod':
            registers[instruction[1]] %= val(instruction[2])
        elif instruction[0] == 'rcv':
            if val(instruction[1]):
                assert played is not None
                return played
        elif instruction[0] == 'jgz':
            if val(instruction[1]) > 0:
                pc += val(instruction[2])
            else:
                pc += 1
            continue

        pc += 1

    raise AssertionError('unreachable')


INPUT_S = '''\
set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2
'''
EXPECTED = 4


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
