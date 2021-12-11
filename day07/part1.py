from __future__ import annotations

import argparse
import os.path

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


class Node:
    def __init__(self, s: str, *, weight: int | None = None) -> None:
        self.s = s
        self.weight = weight
        self.children: list[Node] = []


def compute(s: str) -> str:
    nodes: dict[str, Node] = {}
    parents = {}

    for line in s.splitlines():
        if '->' in line:
            s, children_s = line.split(' -> ')
            children = children_s.split(', ')
        else:
            s = line
            children = []

        s, n_s = s.rstrip(')').split(' (')
        if s in nodes:
            thing = nodes[s]
            thing.weight = int(n_s)
        else:
            thing = nodes[s] = Node(s, weight=int(n_s))

        for child_s in children:
            parents[child_s] = s
            if child_s in nodes:
                child = nodes[child_s]
            else:
                nodes[child_s] = child = Node(child_s)

            thing.children.append(child)

    for k in nodes:
        if k not in parents:
            return k

    raise AssertionError('unreachable')


INPUT_S = '''\
pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
'''
EXPECTED = 'tknk'


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, EXPECTED),
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
