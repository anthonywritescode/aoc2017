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
```
