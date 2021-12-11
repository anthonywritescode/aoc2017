from __future__ import annotations

import argparse
import collections
import operator
import os.path

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

operators = {
    '>=': operator.ge,
    '<=': operator.le,
    '>': operator.gt,
    '<': operator.lt,
    '!=': operator.ne,
    '==': operator.eq,
}
sign = {'inc': 1, 'dec': -1}


def compute(s: str) -> int:
    registers: dict[str, int] = collections.defaultdict(int)

    lines = s.splitlines()
    for line in lines:
        target, adj, num_s, _, src, op, operand_s = line.split()
        if operators[op](registers[src], int(operand_s)):
            registers[target] += sign[adj] * int(num_s)

    return max(registers.values())


INPUT_S = '''\
b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
'''
EXPECTED = 1


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
