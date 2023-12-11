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
1 | 0.8 ± 0.9 | 1.1 ± 0.4 | 2.0 ± 1.0 | 🚀🚀
2 | 1.5 ± 0.9 | 1.6 ± 0.9 | 3.0 ± 2.0 | 🚀
3 | 5.7 ± 0.5 | 4.7 ± 0.4 | 10.4 ± 0.6 | 🐢
4 | 1.06 ± 0.04 | 1.31 ± 0.06 | 2.37 ± 0.09 | 🚀
5 | 0.25 ± 0.02 | 4.35 ± 0.1 | 4.6 ± 0.1 | 🛹
6 | 0.006 ± 0.001 | 0.0022 ± 0.0008 | 0.008 ± 0.002 | 🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
7 | 3.5 ± 0.5 | 3.7 ± 0.4 | 7.2 ± 0.6 | 🛹
8 | 3.56 ± 0.08 | 364.0 ± 5.0 | 368.0 ± 5.0 | 🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢
9 | 2.39 ± 0.06 | 2.43 ± 0.04 | 4.81 ± 0.09 | 🛹
10 | 23.5 ± 0.3 | 31.2 ± 0.5 | 54.7 ± 0.8 | 🐢🐢🐢🐢🐢
11 | 100.0 ± 1.0 | 101.0 ± 1.0 | 201.0 ± 2.0 | 🐢🐢🐢🐢🐢🐢🐢🐢🐢
All days | 142.0 ± 2.0 | 515.0 ± 5.0 | 658.0 ± 6.0 | 
<!-- generated table end -->
