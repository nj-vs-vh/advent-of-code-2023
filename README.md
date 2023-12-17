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
1 | 0.7 ± 0.3 | 1.0 ± 0.3 | 1.7 ± 0.5 | 🚀🚀🚀
2 | 1.3 ± 0.5 | 1.35 ± 0.04 | 2.7 ± 0.5 | 🚀🚀🚀
3 | 5.5 ± 0.4 | 4.5 ± 0.1 | 10.0 ± 0.4 | 🚀
4 | 1.03 ± 0.04 | 1.25 ± 0.04 | 2.28 ± 0.08 | 🚀🚀🚀
5 | 0.25 ± 0.02 | 4.29 ± 0.06 | 4.54 ± 0.08 | 🚀🚀
6 | 0.006 ± 0.002 | 0.0023 ± 0.0007 | 0.008 ± 0.002 | 🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
7 | 3.31 ± 0.1 | 3.7 ± 0.7 | 7.0 ± 0.7 | 🚀
8 | 3.56 ± 0.04 | 351.0 ± 3.0 | 354.0 ± 3.0 | 🐢🐢🐢🐢🐢
9 | 2.4 ± 0.06 | 2.44 ± 0.06 | 4.8 ± 0.1 | 🚀🚀
10 | 23.1 ± 0.2 | 30.5 ± 0.3 | 53.6 ± 0.5 | 🐢🐢
11 | 19.7 ± 0.2 | 21.4 ± 0.1 | 41.1 ± 0.3 | 🐢
12 | 36.0 ± 3.0 | 590.0 ± 10.0 | 620.0 ± 20.0 | 🐢🐢🐢🐢🐢🐢🐢
13 | 8.6 ± 0.1 | 10.9 ± 0.1 | 19.5 ± 0.2 | 🛹
14 | 29.2 ± 0.5 | 3400.0 ± 70.0 | 3430.0 ± 70.0 | 🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢
15 | 1.36 ± 0.02 | 3.62 ± 0.07 | 4.98 ± 0.09 | 🚀🚀
16 | 15.0 ± 10.0 | 2790.0 ± 30.0 | 2800.0 ± 30.0 | 🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢
17 | 512.0 ± 8.0 | 1720.0 ± 30.0 | 2230.0 ± 30.0 | 🐢🐢🐢🐢🐢🐢🐢🐢🐢
All days | 660.0 ± 10.0 | 8930.0 ± 80.0 | 9590.0 ± 80.0 | 
<!-- generated table end -->
