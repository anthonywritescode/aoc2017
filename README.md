[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/anthonywritescode/aoc2017/main.svg)](https://results.pre-commit.ci/latest/github/anthonywritescode/aoc2017/main)

advent of code 2017
===================

https://adventofcode.com/2017

### stream / youtube

- [Streamed daily on twitch](https://twitch.tv/anthonywritescode)
- [Streams uploaded to youtube afterwards](https://www.youtube.com/channel/UChPxcypesw8L-iqltstSI4Q)
- [Uploaded to youtube afterwards](https://www.youtube.com/anthonywritescode)

### about

for 2017, I'm doing this in 2021

### timing

- comparing to these numbers isn't necessarily useful
- normalize your timing to day 1 part 1 and compare
- alternate implementations are listed in parens
- these timings are very non-scientific (sample size 1)

```console
$ find -maxdepth 1 -type d -name 'day*' -not -name day00 | sort | xargs --replace bash -xc 'python {}/part1.py {}/input.txt; python {}/part2.py {}/input.txt'
+ python day01/part1.py day01/input.txt
1393
> 575 μs
+ python day01/part2.py day01/input.txt
1292
> 919 μs
+ python day02/part1.py day02/input.txt
21845
> 134 μs
+ python day02/part2.py day02/input.txt
191
> 1234 μs
+ python day03/part1.py day03/input.txt
552
> 157 μs
+ python day03/part2.py day03/input.txt
330785
> 438 μs
+ python day04/part1.py day04/input.txt
477
> 846 μs
+ python day04/part2.py day04/input.txt
167
> 3924 μs
+ python day05/part1.py day05/input.txt
373160
> 225 ms
+ python day05/part2.py day05/input.txt
26395586
> 18743 ms
+ python day06/part1.py day06/input.txt
6681
> 51390 μs
+ python day06/part2.py day06/input.txt
2392
> 50837 μs
+ python day07/part1.py day07/input.txt
ykpsek
> 5124 μs
+ python day07/part2.py day07/input.txt
1060
> 5808 μs
+ python day08/part1.py day08/input.txt
5946
> 1479 μs
+ python day08/part2.py day08/input.txt
6026
> 1727 μs
+ python day09/part1.py day09/input.txt
13154
> 6649 μs
+ python day09/part2.py day09/input.txt
6369
> 5609 μs
+ python day10/part1.py day10/input.txt
13760
> 79 μs
+ python day10/part2.py day10/input.txt
2da93395f1a6bb3472203252e3b17fe5
> 4405 μs
+ python day11/part1.py day11/input.txt
818
> 2948 μs
+ python day11/part2.py day11/input.txt
1596
> 8003 μs
+ python day12/part1.py day12/input.txt
378
> 4597 μs
+ python day12/part2.py day12/input.txt
204
> 9608 μs
+ python day13/part1.py day13/input.txt
2384
> 2641 μs
+ python day13/part2.py day13/input.txt
3921270
> 5742 ms (brute force)
+ python day14/part1.py day14/input.txt
8316
> 221 ms
+ python day14/part2.py day14/input.txt
1074
> 275 ms
+ python day15/part1.py day15/input.txt
619
> 31194 ms
+ python day15/part2.py day15/input.txt
290
> 24481 ms
+ python day16/part1.py day16/input.txt
hmefajngplkidocb
> 62156 μs
+ python day16/part2.py day16/input.txt
fbidepghmjklcnoa
> 4074 ms
+ python day17/part1.py day17/input.txt
355
> 1277 μs
+ python day17/part2.py day17/input.txt
6154117
> 19327 ms
+ python day18/part1.py day18/input.txt
3423
> 1503 μs
+ python day18/part2.py day18/input.txt
7493
> 175 ms
+ python day19/part1.py day19/input.txt
SXPZDFJNRL
> 11119 μs
+ python day19/part2.py day19/input.txt
18126
> 9712 μs
+ python day20/part1.py day20/input.txt
243
> 28414 μs
+ python day20/part2.py day20/input.txt
648
> 2076 ms
+ python day21/part1.py day21/input.txt
171
> 9892 μs
+ python day21/part2.py day21/input.txt
2498142
> 11509 ms
+ python day22/part1.py day22/input.txt
5266
> 9577 μs
+ python day22/part2.py day22/input.txt
2511895
> 13415 ms
+ python day23/part1.py day23/input.txt
6241
> 44859 μs
+ python day23/part2.py day23/input.txt
909
> 6776 μs
+ python day24/part1.py day24/input.txt
1511
> 7193 ms
+ python day24/part2.py day24/input.txt
1471
> 7278 ms
```
