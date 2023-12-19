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
1 | 0.6 ± 0.2 | 0.94 ± 0.04 | 1.6 ± 0.2 | 🚀🚀🚀
2 | 2.0 ± 1.0 | 1.5 ± 0.2 | 3.0 ± 1.0 | 🚀🚀🚀
3 | 5.9 ± 0.4 | 4.9 ± 0.2 | 10.8 ± 0.5 | 🚀
4 | 1.08 ± 0.06 | 1.31 ± 0.07 | 2.4 ± 0.1 | 🚀🚀🚀
5 | 0.27 ± 0.02 | 4.6 ± 0.2 | 4.8 ± 0.2 | 🚀🚀
6 | 0.007 ± 0.003 | 0.0025 ± 0.0009 | 0.009 ± 0.004 | 🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
7 | 3.6 ± 0.2 | 3.9 ± 0.8 | 7.5 ± 0.8 | 🚀
8 | 3.6 ± 0.07 | 363.0 ± 8.0 | 366.0 ± 8.0 | 🐢🐢🐢🐢🐢
9 | 2.43 ± 0.05 | 2.49 ± 0.07 | 4.92 ± 0.09 | 🚀🚀
10 | 23.6 ± 0.4 | 31.2 ± 0.5 | 54.8 ± 0.7 | 🐢🐢
11 | 20.0 ± 0.2 | 21.7 ± 0.2 | 41.8 ± 0.4 | 🐢
12 | 37.0 ± 3.0 | 610.0 ± 30.0 | 650.0 ± 30.0 | 🐢🐢🐢🐢🐢🐢🐢
13 | 8.9 ± 0.1 | 11.3 ± 0.2 | 20.2 ± 0.3 | 🛹
14 | 29.0 ± 0.4 | 3660.0 ± 50.0 | 3690.0 ± 50.0 | 🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢
15 | 1.34 ± 0.02 | 3.57 ± 0.08 | 4.91 ± 0.09 | 🚀🚀
16 | 15.0 ± 10.0 | 2750.0 ± 50.0 | 2760.0 ± 50.0 | 🐢🐢🐢🐢🐢🐢🐢🐢🐢
17 | 540.0 ± 30.0 | 1870.0 ± 90.0 | 2400.0 ± 100.0 | 🐢🐢🐢🐢🐢🐢🐢🐢🐢
18 | 12.7 ± 0.6 | 20.0 ± 10.0 | 32.0 ± 10.0 | 🐢
19 | 4.0 ± 10.0 | 10.0 ± 10.0 | 10.0 ± 20.0 | 🚀
All days | 710.0 ± 30.0 | 9400.0 ± 100.0 | 10100.0 ± 100.0 | 
<!-- generated table end -->
