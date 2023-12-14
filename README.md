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
1 | 0.8 ± 0.5 | 1.3 ± 0.9 | 2.0 ± 1.0 | 🚀🚀🚀
2 | 1.5 ± 0.7 | 1.6 ± 0.7 | 3.0 ± 1.0 | 🚀🚀
3 | 5.7 ± 0.4 | 4.5 ± 0.1 | 10.2 ± 0.4 | 🛹
4 | 1.04 ± 0.03 | 1.27 ± 0.05 | 2.31 ± 0.07 | 🚀🚀
5 | 0.25 ± 0.02 | 4.28 ± 0.06 | 4.53 ± 0.07 | 🚀
6 | 0.006 ± 0.002 | 0.0022 ± 0.0007 | 0.008 ± 0.002 | 🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
7 | 3.4 ± 0.1 | 3.8 ± 0.7 | 7.1 ± 0.7 | 🚀
8 | 3.65 ± 0.07 | 342.0 ± 6.0 | 345.0 ± 6.0 | 🐢🐢🐢🐢🐢🐢
9 | 2.49 ± 0.08 | 2.49 ± 0.06 | 5.0 ± 0.1 | 🚀
10 | 23.8 ± 0.6 | 31.6 ± 0.7 | 55.0 ± 1.0 | 🐢🐢
11 | 19.8 ± 0.2 | 21.3 ± 0.2 | 41.2 ± 0.3 | 🐢🐢
12 | 38.0 ± 3.0 | 630.0 ± 30.0 | 670.0 ± 30.0 | 🐢🐢🐢🐢🐢🐢🐢
13 | 9.0 ± 0.2 | 11.4 ± 0.3 | 20.4 ± 0.4 | 🐢
14 | 11.0 ± 0.4 | 4200.0 ± 100.0 | 4200.0 ± 100.0 | 🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢
All days | 121.0 ± 3.0 | 5300.0 ± 100.0 | 5400.0 ± 100.0 | 
<!-- generated table end -->
