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
1 | 0.7 ± 0.3 | 1.1 ± 0.4 | 1.8 ± 0.7 | 🚀🚀
2 | 1.3 ± 0.6 | 1.36 ± 0.06 | 2.7 ± 0.6 | 🚀🚀
3 | 5.7 ± 0.5 | 4.8 ± 0.4 | 10.5 ± 0.7 | 🛹
4 | 1.05 ± 0.04 | 1.29 ± 0.06 | 2.35 ± 0.08 | 🚀🚀
5 | 0.25 ± 0.02 | 4.32 ± 0.08 | 4.57 ± 0.09 | 🚀
6 | 0.006 ± 0.002 | 0.003 ± 0.003 | 0.008 ± 0.004 | 🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
7 | 3.5 ± 0.4 | 3.7 ± 0.4 | 7.1 ± 0.6 | 🛹
8 | 3.56 ± 0.08 | 338.0 ± 3.0 | 341.0 ± 3.0 | 🐢🐢🐢🐢🐢🐢🐢🐢
9 | 2.41 ± 0.05 | 2.44 ± 0.04 | 4.85 ± 0.08 | 🚀
10 | 23.3 ± 0.3 | 30.7 ± 0.6 | 54.0 ± 0.8 | 🐢🐢🐢🐢
11 | 19.9 ± 0.3 | 21.3 ± 0.4 | 41.2 ± 0.5 | 🐢🐢🐢🐢
12 | 38.0 ± 4.0 | 620.0 ± 20.0 | 660.0 ± 20.0 | 🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢
13 | 8.9 ± 0.2 | 13.0 ± 8.0 | 21.0 ± 8.0 | 🐢🐢
All days | 109.0 ± 4.0 | 1050.0 ± 20.0 | 1160.0 ± 20.0 | 
<!-- generated table end -->
