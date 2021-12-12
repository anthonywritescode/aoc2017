from __future__ import annotations

import argparse
import collections
import math
import os.path
from typing import NamedTuple

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def is_int(f: float) -> bool:
    return abs(f - round(f)) < .00001


class Point(NamedTuple):
    pid: int
    p: tuple[int, int, int]
    v: tuple[int, int, int]
    a: tuple[int, int, int]

    def y(self, t: int) -> float:
        return (
            self.p[1] +
            (self.v[1] + self.a[1] / 2) * t +
            (self.a[1] / 2) * t * t
        )

    def z(self, t: int) -> float:
        return (
            self.p[2] +
            (self.v[2] + self.a[2] / 2) * t +
            (self.a[2] / 2) * t * t
        )

    def collides(self, other: Point) -> int | None:
        x_a = (.5 * self.a[0] - .5 * other.a[0])
        x_b = ((self.v[0] + self.a[0] / 2) - (other.v[0] + other.a[0] / 2))
        x_c = (self.p[0] - other.p[0])

        if (x_b * x_b - 4 * x_a * x_c) < 0:
            return None

        possible = []

        if x_a == 0 and x_b == 0:
            return None
        elif x_a == 0:
            sln = -x_c / x_b
            if is_int(sln):
                possible.append(round(sln))
        else:
            possible = []
            for mult in (-1, 1):
                sln = (
                    -x_b + mult * math.sqrt(x_b * x_b - 4 * x_a * x_c)
                ) / (2 * x_a)
                if sln > 0 and is_int(sln):
                    possible.append(round(sln))

        for cand in possible:
            if (
                self.y(cand) == other.y(cand) and
                self.z(cand) == other.z(cand)
            ):
                return cand
        else:
            return None

    @classmethod
    def parse(cls, i: int, s: str) -> Point:
        p_s, v_s, a_s = s.split(', ')
        _, p_s = p_s.rstrip('>').split('<')
        _, v_s = v_s.rstrip('>').split('<')
        _, a_s = a_s.rstrip('>').split('<')
        p_x_s, p_y_s, p_z_s = p_s.split(',')
        v_x_s, v_y_s, v_z_s = v_s.split(',')
        a_x_s, a_y_s, a_z_s = a_s.split(',')

        return cls(
            i,
            (int(p_x_s), int(p_y_s), int(p_z_s)),
            (int(v_x_s), int(v_y_s), int(v_z_s)),
            (int(a_x_s), int(a_y_s), int(a_z_s)),
        )


def compute(s: str) -> int:
    points = [Point.parse(i, line) for i, line in enumerate(s.splitlines())]

    collisions: dict[int, set[int]] = collections.defaultdict(set)
    for i, point in enumerate(points):
        for j, other in enumerate(points[i + 1:], i + 1):
            collides = point.collides(other)
            if collides is not None:
                collisions[collides].update((i, j))

    remaining = set(range(len(points)))
    for t, collision in sorted(collisions.items()):
        if len(collision & remaining) >= 2:
            remaining -= collision

    return len(remaining)


INPUT_S = '''\
p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>
p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>
p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>
p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>
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


def test_collide() -> None:
    p1 = Point.parse(1, 'p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>')
    p2 = Point.parse(2, 'p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>')
    assert p1.collides(p2) == 2


def test_collide2() -> None:
    p1 = Point.parse(1, 'p=<1199,-2918,1457>, v=<-13,115,-8>, a=<-7,8,-10>')
    p2 = Point.parse(2, 'p=<2551,2418,-1471>, v=<-106,-108,39>, a=<-6,-5,6>')
    assert p1.collides(p2) == 16


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f, timing():
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
