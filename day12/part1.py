from __future__ import annotations

import argparse
import collections
import os.path

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    edges = collections.defaultdict(list)

    for line in s.splitlines():
        src, dest_s = line.split(' <-> ')
        dests = dest_s.split(', ')

        for dest in dests:
            edges[src].append(dest)
            edges[dest].append(src)

    seen = set()
    todo = ['0']
    while todo:
        node = todo.pop()
        seen.add(node)
        todo.extend(child for child in edges[node] if child not in seen)

    return len(seen)


INPUT_S = '''\
0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5
'''
EXPECTED = 6


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
