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
1 | 0.7 ± 0.3 | 1.1 ± 0.4 | 1.8 ± 0.6 | 🚀🚀
2 | 1.3 ± 0.6 | 1.5 ± 0.5 | 3.0 ± 1.0 | 🚀
3 | 5.7 ± 0.5 | 4.7 ± 0.4 | 10.4 ± 0.6 | 🐢
4 | 1.06 ± 0.05 | 1.29 ± 0.06 | 2.36 ± 0.09 | 🚀🚀
5 | 0.27 ± 0.03 | 4.6 ± 0.4 | 4.8 ± 0.4 | 🚀
6 | 0.007 ± 0.003 | 0.0023 ± 0.0007 | 0.009 ± 0.003 | 🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
7 | 3.6 ± 0.6 | 3.7 ± 0.5 | 7.3 ± 0.7 | 🛹
8 | 3.7 ± 0.1 | 360.0 ± 8.0 | 364.0 ± 8.0 | 🐢🐢🐢🐢🐢🐢🐢🐢
9 | 2.4 ± 0.05 | 2.43 ± 0.06 | 4.83 ± 0.1 | 🚀
10 | 24.0 ± 0.5 | 31.6 ± 1.0 | 56.0 ± 1.0 | 🐢🐢🐢🐢
11 | 388.0 ± 8.0 | 390.0 ± 8.0 | 780.0 ± 10.0 | 🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢
All days | 431.0 ± 8.0 | 801.0 ± 10.0 | 1230.0 ± 10.0 | 
<!-- generated table end -->
