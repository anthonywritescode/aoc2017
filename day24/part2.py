from __future__ import annotations

import argparse
import os.path

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    edges = set()

    for line in s.splitlines():
        s1, s2 = line.split('/')
        n1, n2 = int(s1), int(s2)
        edges.add((n1, n2))

    paths = []

    todo: list[tuple[tuple[int, ...], frozenset[tuple[int, int]]]]
    todo = [((0,), frozenset(edges))]
    while todo:
        path, edges_left = todo.pop()

        added = False
        for candidate in (pair for pair in edges_left if path[-1] in pair):
            if path[-1] == candidate[0]:
                next_n = candidate[1]
            else:
                next_n = candidate[0]
            todo.append(((*path, next_n), frozenset(edges_left - {candidate})))
            added = True
        if not added:
            paths.append(path)

    paths.sort(key=lambda p: len(p))
    return max(
        sum(path[:-1]) * 2 + path[-1]
        for path in paths
        if len(path) == len(paths[-1])
    )


INPUT_S = '''\
0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10
'''
EXPECTED = 19


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
