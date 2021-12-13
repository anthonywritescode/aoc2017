from __future__ import annotations

import argparse
import collections
import os.path
from typing import NamedTuple

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

START = '.#./..#/###'


def _rotate(x: float, y: float, size: int) -> tuple[int, int]:
    mid_x, mid_y = ((size - 1) / 2, (size - 1) / 2)
    x, y = x - mid_x, y - mid_y
    x, y = (y, -x)
    x, y = round(x + mid_y), round(y + mid_y)
    return x, y


class MiniGrid(NamedTuple):
    size: int
    coords: frozenset[tuple[int, int]]

    def print_grid(self) -> None:
        for y in range(self.size):
            for x in range(self.size):
                print('#' if (x, y) in self.coords else '.', end='')
            print()

    def gen_key(self) -> set[MiniGrid]:
        # original
        ret = {self}
        # flip x
        coords = frozenset(((self.size - 1 - x), y) for x, y in self.coords)
        ret.add(self._replace(coords=coords))
        # flip y
        coords = frozenset((x, (self.size - 1 - y)) for x, y in coords)
        ret.add(self._replace(coords=coords))

        # rotate 90
        # rotate 180
        # rotate 270
        coords = self.coords
        for _ in range(3):
            coords = frozenset(_rotate(x, y, self.size) for x, y in coords)
            ret.add(self._replace(coords=coords))
            # flip x of rotate ???
            coords = frozenset(((self.size - 1 - x), y) for x, y in coords)
            ret.add(self._replace(coords=coords))
            # flip y of rotate ???
            coords = frozenset((x, (self.size - 1 - y)) for x, y in coords)
            ret.add(self._replace(coords=coords))

        return ret

    @classmethod
    def parse(cls, s: str) -> MiniGrid:
        parts = s.split('/')
        coords = frozenset(
            (x, y)
            for y, part in enumerate(parts)
            for x, c in enumerate(part)
            if c == '#'
        )
        return cls(len(parts), coords)


def to_megagrid(grid: list[list[MiniGrid]]) -> MiniGrid:
    inner_size = grid[0][0].size
    coords = frozenset(
        (inner_x + inner_size * x, inner_y + inner_size * y)
        for y, row in enumerate(grid)
        for x, mini_grid in enumerate(row)
        for inner_x, inner_y in mini_grid.coords
    )
    return MiniGrid(inner_size * len(grid[0]), coords)


def to_n_grid(mega_grid: MiniGrid, size: int) -> list[list[MiniGrid]]:
    grid_size = mega_grid.size // size
    points = collections.defaultdict(set)
    for x, y in mega_grid.coords:
        points[x // size, y // size].add((x % size, y % size))
    return [
        [MiniGrid(size, frozenset(points[x, y])) for x in range(grid_size)]
        for y in range(grid_size)
    ]


def compute(s: str, *, iterations: int = 5) -> int:
    rules = {}
    for line in s.splitlines():
        src, dst = line.split(' => ')
        src_minigrid = MiniGrid.parse(src)
        dst_minigrid = MiniGrid.parse(dst)

        for key in src_minigrid.gen_key():
            rules[key] = dst_minigrid

    grid = [[MiniGrid.parse(START)]]
    for _ in range(iterations):
        size = sum(item[0] for item in grid[0])

        # proper sizing
        for target_size in (2, 3):
            if size % target_size == 0 and grid[0][0].size != target_size:
                grid = to_n_grid(to_megagrid(grid), target_size)
                break

        grid = [[rules[item] for item in row] for row in grid]

    return sum(len(coords) for row in grid for _, coords in row)


INPUT_S = '''\
../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#
'''
EXPECTED = 12


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, EXPECTED),
    ),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s, iterations=2) == expected


@pytest.mark.parametrize(
    ('coord', 'size', 'expected'),
    (
        ((1, 1), 2, (1, 0)),
        ((1, 0), 2, (0, 0)),
        ((2, 1), 3, (1, 0)),
        ((1, 0), 3, (0, 1)),
    ),
)
def test_rotate(
        coord: tuple[int, int],
        size: int,
        expected: tuple[int, int],
) -> None:
    assert _rotate(*coord, size) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f, timing():
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
