from __future__ import annotations

import argparse
import collections
import os.path

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    tape: dict[int, int] = collections.defaultdict(int)

    initial, *rest = s.split('\n\n')
    state = initial.splitlines()[0][-2]
    _, steps_s, _ = initial.splitlines()[1].rsplit(' ', 2)

    progs = {}
    for prog_s in rest:
        lines = prog_s.splitlines()
        prog_id = lines[0][-2]
        assert lines[1][-2] == '0'
        if_zero_w = int(lines[2][-2])
        if_zero_d = -1 if lines[3].split()[-1] == 'left.' else 1
        if_zero_s = lines[4][-2]
        assert lines[5][-2] == '1'
        if_one_w = int(lines[6][-2])
        if_one_d = -1 if lines[7].split()[-1] == 'left.' else 1
        if_one_s = lines[8][-2]

        progs[prog_id] = (
            (if_zero_w, if_zero_d, if_zero_s),
            (if_one_w, if_one_d, if_one_s),
        )

    pos = 0
    for _ in range(int(steps_s)):
        prog = progs[state]
        write, direction, state = prog[tape[pos]]
        tape[pos] = write
        pos += direction

    return sum(tape.values())


INPUT_S = '''\
Begin in state A.
Perform a diagnostic checksum after 6 steps.

In state A:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state B.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state B.

In state B:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state A.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state A.
'''
EXPECTED = 3


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
