# Advent of Code 2023

This year I've decided to pause my attempts to learn Rust and just focus on solving the challenges.
I'm going to use Python, which I know and love, and to make my solutions
- clean
- readable
- fully typed
- reasonably performant
- zero-dependency (except for visualizations, which are done separately)
- single-threaded Python

```shell
python run.py <day number> [--debug [--input custom-input.txt [--part 1]]]
```

## Performance measurement

Just for fun, this year I'm keeping track of how long my solutions take to run. Later I might take some time to
optimize them and update the numbers.

Methodology:
- Measured time: between the moment string input is read from the disk and the moment the answer is calculated
- Each part is measured independently, no data is shared between parts (i.e. input parsing is included in both times)
- Averaged over 50 runs
- System: 2021 Mac M1 Pro 16 Gb 

### Results

Updated as days go with `python measure_performance.py`

<!-- generated table start -->
**Day** | **Part 1**, msec | **Part 2**, msec | **Total**, msec | **Relative score**
---: | :---: | :---: | :---: | ---
1 | 0.8 ± 0.5 | 1.2 ± 0.5 | 2.0 ± 0.9 | 🚀🚀
2 | 1.5 ± 0.7 | 1.7 ± 1.0 | 3.0 ± 2.0 | 🚀
3 | 5.7 ± 0.5 | 4.6 ± 0.4 | 10.3 ± 0.7 | 🐢
4 | 1.07 ± 0.05 | 1.31 ± 0.07 | 2.38 ± 0.1 | 🚀
5 | 0.26 ± 0.02 | 4.36 ± 0.08 | 4.61 ± 0.09 | 🛹
6 | 0.006 ± 0.002 | 0.0023 ± 0.0006 | 0.009 ± 0.002 | 🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
7 | 3.5 ± 0.5 | 3.8 ± 0.6 | 7.3 ± 0.7 | 🐢
8 | 3.59 ± 0.08 | 349.0 ± 4.0 | 352.0 ± 4.0 | 🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢
9 | 2.38 ± 0.04 | 2.43 ± 0.03 | 4.8 ± 0.07 | 🛹
10 | 23.5 ± 0.2 | 30.7 ± 0.2 | 54.2 ± 0.4 | 🐢🐢🐢🐢🐢
11 | 20.1 ± 0.3 | 21.6 ± 0.4 | 41.7 ± 0.6 | 🐢🐢🐢🐢🐢
All days | 62.0 ± 1.0 | 420.0 ± 5.0 | 483.0 ± 5.0 | 
<!-- generated table end -->
