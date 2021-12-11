from __future__ import annotations

import argparse
import math
import os.path
from typing import NamedTuple

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def sign(n: int) -> int:
    if n >= 0:
        return 1
    else:
        return -1


class Point(NamedTuple):
    pos: tuple[int, int, int]
    v: tuple[int, int, int]
    a: tuple[int, int, int]

    def minimum_time(self) -> float:
        t = 0.
        for d in (0, 1, 2):
            p, v, a = self.pos[d], self.v[d], self.a[d]

            if sign(p) == sign(v) == sign(a):
                continue

            if sign(v) != sign(a) and a != 0:
                t = max(t, -v / a)

            if sign(p) != sign(a) and a != 0:
                for mult in (-1, 1):
                    t = max(t, (-v + mult * math.sqrt(v * v - 2 * a * p)) / a)
            elif sign(p) != sign(a) and a == 0 and v != 0:
                t = max(t, -p / v)
        return t

    def p_at(self, t: float) -> tuple[float, float, float]:
        return (
            self.pos[0] + self.v[0] * t + .5 * self.a[0] * t * t,
            self.pos[1] + self.v[1] * t + .5 * self.a[1] * t * t,
            self.pos[2] + self.v[2] * t + .5 * self.a[2] * t * t,
        )

    def v_at(self, t: float) -> tuple[float, float, float]:
        return (
            self.v[0] + self.a[0] * t,
            self.v[1] + self.a[1] * t,
            self.v[2] + self.a[2] * t,
        )

    def distance(self, t: int) -> float:
        return sum(abs(x) for x in self.p_at(t))

    def sort_key(self, t: int) -> tuple[float, float, float]:
        return (
            sum(abs(x) for x in self.a),
            sum(abs(x) for x in self.v_at(t)),
            self.distance(t),
        )

    @classmethod
    def parse(cls, s: str) -> Point:
        p_s, v_s, a_s = s.split(', ')
        _, p_s = p_s.rstrip('>').split('<')
        _, v_s = v_s.rstrip('>').split('<')
        _, a_s = a_s.rstrip('>').split('<')
        p_x_s, p_y_s, p_z_s = p_s.split(',')
        v_x_s, v_y_s, v_z_s = v_s.split(',')
        a_x_s, a_y_s, a_z_s = a_s.split(',')

        return cls(
            (int(p_x_s), int(p_y_s), int(p_z_s)),
            (int(v_x_s), int(v_y_s), int(v_z_s)),
            (int(a_x_s), int(a_y_s), int(a_z_s)),
        )


def compute(s: str) -> int:
    points = [Point.parse(line) for line in s.splitlines()]

    t = max(round(point.minimum_time()) for point in points)

    points_at_t = [(p.sort_key(t), p) for p in points]
    _, p = min(points_at_t)

    return points.index(p)


INPUT_S = '''\
p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>
p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>
'''
EXPECTED = 0


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, EXPECTED),
    ),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


@pytest.mark.parametrize(
    ('pt', 'expected'),
    (
        (
            Point(pos=(-2089, -239, 1142), v=(52, 12, 3), a=(7, 0, -7)),
            19.91666,
        ),
    ),
)
def test_minimum_time(pt: Point, expected: float) -> None:
    assert pt.minimum_time() == pytest.approx(expected)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f, timing():
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
