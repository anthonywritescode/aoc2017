from __future__ import annotations

import argparse
import os.path

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str, *, size: int = 16) -> str:
    chars = {chr(ord('a') + i): i for i in range(size)}

    for part in s.strip().split(','):
        if part[0] == 's':
            n = int(part[1:])
            chars = {k: (v + n) % size for k, v in chars.items()}
        elif part[0] == 'x':
            n1_s, n2_s = part[1:].split('/')
            c1, = (k for k, v in chars.items() if v == int(n1_s))
            c2, = (k for k, v in chars.items() if v == int(n2_s))
            chars[c1], chars[c2] = chars[c2], chars[c1]
        elif part[0] == 'p':
            c1, c2 = part[1:].split('/')
            chars[c1], chars[c2] = chars[c2], chars[c1]
        else:
            raise AssertionError(part)

    inv = {v: k for k, v in chars.items()}
    return ''.join(inv[i] for i in range(size))


INPUT_S = '''\
s1,x3/4,pe/b
'''
EXPECTED = 'baedc'


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, EXPECTED),
    ),
)
def test(input_s: str, expected: str) -> None:
    assert compute(input_s, size=5) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f, timing():
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
