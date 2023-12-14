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
1 | 0.7 ± 0.3 | 1.1 ± 0.5 | 1.8 ± 0.8 | 🚀🚀🚀
2 | 1.3 ± 0.4 | 1.5 ± 0.5 | 2.8 ± 0.6 | 🚀🚀
3 | 6.0 ± 1.0 | 4.8 ± 0.4 | 11.0 ± 2.0 | 🛹
4 | 1.04 ± 0.03 | 1.28 ± 0.07 | 2.32 ± 0.08 | 🚀🚀
5 | 0.25 ± 0.02 | 4.3 ± 0.09 | 4.56 ± 0.1 | 🚀
6 | 0.006 ± 0.003 | 0.002 ± 0.001 | 0.008 ± 0.004 | 🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
7 | 3.5 ± 0.2 | 3.9 ± 0.7 | 7.4 ± 0.8 | 🚀
8 | 3.7 ± 0.1 | 360.0 ± 7.0 | 364.0 ± 7.0 | 🐢🐢🐢🐢🐢🐢
9 | 2.5 ± 0.1 | 2.56 ± 0.08 | 5.1 ± 0.1 | 🚀
10 | 24.4 ± 0.9 | 32.0 ± 1.0 | 57.0 ± 2.0 | 🐢🐢🐢
11 | 20.3 ± 0.4 | 22.1 ± 0.4 | 42.4 ± 0.8 | 🐢🐢
12 | 38.0 ± 3.0 | 610.0 ± 30.0 | 650.0 ± 30.0 | 🐢🐢🐢🐢🐢🐢🐢
13 | 8.9 ± 0.2 | 11.3 ± 0.2 | 20.1 ± 0.4 | 🐢
14 | 29.5 ± 0.6 | 3420.0 ± 80.0 | 3450.0 ± 80.0 | 🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢
All days | 139.0 ± 3.0 | 4480.0 ± 80.0 | 4610.0 ± 90.0 | 
<!-- generated table end -->
