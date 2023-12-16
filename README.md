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
- Averaged over 30 runs
- System: 2021 Mac M1 Pro 16 Gb 

### Results

Updated as days go with `python measure_performance.py`

<!-- generated table start -->
**Day** | **Part 1**, msec | **Part 2**, msec | **Total**, msec | **Relative score**
---: | :---: | :---: | :---: | ---
1 | 0.6 ± 0.03 | 1.1 ± 1.0 | 1.7 ± 1.0 | 🚀🚀🚀
2 | 1.3 ± 0.4 | 1.32 ± 0.04 | 2.6 ± 0.4 | 🚀🚀
3 | 5.5 ± 0.4 | 4.5 ± 0.2 | 10.0 ± 0.5 | 🚀
4 | 1.04 ± 0.03 | 1.27 ± 0.06 | 2.31 ± 0.09 | 🚀🚀🚀
5 | 0.25 ± 0.02 | 4.3 ± 0.08 | 4.56 ± 0.09 | 🚀🚀
6 | 0.006 ± 0.002 | 0.002 ± 0.001 | 0.008 ± 0.003 | 🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
7 | 3.3 ± 0.1 | 3.7 ± 0.6 | 7.0 ± 0.7 | 🚀
8 | 3.57 ± 0.06 | 334.0 ± 2.0 | 338.0 ± 2.0 | 🐢🐢🐢🐢🐢🐢
9 | 2.41 ± 0.05 | 2.44 ± 0.02 | 4.85 ± 0.06 | 🚀🚀
10 | 22.8 ± 0.2 | 30.1 ± 0.2 | 52.9 ± 0.4 | 🐢🐢
11 | 19.8 ± 0.1 | 21.3 ± 0.1 | 41.1 ± 0.2 | 🐢🐢
12 | 36.0 ± 3.0 | 580.0 ± 10.0 | 620.0 ± 20.0 | 🐢🐢🐢🐢🐢🐢🐢
13 | 8.6 ± 0.1 | 11.0 ± 0.1 | 19.6 ± 0.2 | 🛹
14 | 29.2 ± 0.3 | 3620.0 ± 30.0 | 3650.0 ± 30.0 | 🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢
15 | 1.35 ± 0.03 | 3.56 ± 0.08 | 4.9 ± 0.1 | 🚀🚀
16 | 14.0 ± 10.0 | 2730.0 ± 30.0 | 2740.0 ± 30.0 | 🐢🐢🐢🐢🐢🐢🐢🐢🐢
All days | 150.0 ± 10.0 | 7350.0 ± 40.0 | 7500.0 ± 40.0 | 
<!-- generated table end -->
