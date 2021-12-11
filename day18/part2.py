from __future__ import annotations

import argparse
import collections
import contextlib
import os.path

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


class Prog:
    def __init__(self, pid: int) -> None:
        self.reg = collections.defaultdict(int)
        self.reg['p'] = pid
        self.pc = 0
        self.sent = 0
        self.w_q: collections.deque[int] = collections.deque()
        self.r_q: collections.deque[int] = collections.deque()


def run(prog: Prog, instructions: list[list[str]]) -> int:
    def val(op: str) -> int:
        if op.isalpha():
            return prog.reg[op]
        else:
            return int(op)

    while True:
        instruction = instructions[prog.pc]
        if instruction[0] == 'snd':
            prog.w_q.append(val(instruction[1]))
            prog.sent += 1
        elif instruction[0] == 'set':
            prog.reg[instruction[1]] = val(instruction[2])
        elif instruction[0] == 'add':
            prog.reg[instruction[1]] += val(instruction[2])
        elif instruction[0] == 'mul':
            prog.reg[instruction[1]] *= val(instruction[2])
        elif instruction[0] == 'mod':
            prog.reg[instruction[1]] %= val(instruction[2])
        elif instruction[0] == 'rcv':
            prog.reg[instruction[1]] = prog.r_q.popleft()
        elif instruction[0] == 'jgz':
            if val(instruction[1]) > 0:
                prog.pc += val(instruction[2])
            else:
                prog.pc += 1
            continue

        prog.pc += 1


def compute(s: str) -> int:
    instructions = [line.split() for line in s.splitlines()]

    progs = [Prog(0), Prog(1)]
    progs[0].r_q = progs[1].w_q
    progs[1].r_q = progs[0].w_q

    while True:
        before = [prog.sent for prog in progs]
        for prog in progs:
            with contextlib.suppress(IndexError):
                run(prog, instructions)
        after = [prog.sent for prog in progs]
        if after == before:
            break

    return progs[1].sent


INPUT_S = '''\
snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d
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
