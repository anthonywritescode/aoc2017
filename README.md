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
```
