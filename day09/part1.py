from __future__ import annotations

import argparse
import os.path
from typing import Any

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    s = s.strip()
    assert s[0] == '{'

    # XXX: recursive type
    root: list[Any] = []
    stack = [root]
    in_garbage = False
    in_escape = False
    for c in s[1:]:
        if in_garbage and not in_escape and c == '>':
            in_garbage = False
        elif in_garbage and not in_escape and c == '!':
            in_escape = True
        elif in_escape:
            in_escape = False
        elif in_garbage:
            continue
        elif c == '<':
            in_garbage = True
        elif c == '{':
            # XXX: recursive type
            new_group: list[Any] = []
            stack[-1].append(new_group)
            stack.append(new_group)
        elif c == '}':
            stack.pop()

    assert not stack

    total = 0
    todo = [(1, root)]
    while todo:
        next_n, next_group = todo.pop()
        total += next_n
        todo.extend((next_n + 1, child) for child in next_group)

    return total


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        ('{}', 1),
        ('{{{}}}', 6),
        ('{{},{}}', 5),
        ('{{{},{},{{}}}}', 16),
        ('{<a>,<a>,<a>,<a>}', 1),
        ('{{<ab>},{<ab>},{<ab>},{<ab>}}', 9),
        ('{{<!!>},{<!!>},{<!!>},{<!!>}}', 9),
        ('{{<a!>},{<a!>},{<a!>},{<ab>}}', 3),
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
