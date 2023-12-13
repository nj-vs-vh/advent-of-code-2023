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
1 | 0.7 ± 0.2 | 1.1 ± 0.4 | 1.7 ± 0.6 | 🚀🚀
2 | 1.5 ± 1.0 | 1.5 ± 0.4 | 3.0 ± 1.0 | 🚀🚀
3 | 5.6 ± 0.5 | 4.6 ± 0.4 | 10.2 ± 0.7 | 🛹
4 | 1.07 ± 0.04 | 1.31 ± 0.06 | 2.37 ± 0.08 | 🚀🚀
5 | 0.25 ± 0.03 | 4.29 ± 0.1 | 4.5 ± 0.1 | 🚀
6 | 0.006 ± 0.001 | 0.0021 ± 0.0005 | 0.008 ± 0.002 | 🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
7 | 3.5 ± 0.5 | 3.7 ± 0.4 | 7.2 ± 0.6 | 🛹
8 | 3.63 ± 0.1 | 357.0 ± 6.0 | 361.0 ± 6.0 | 🐢🐢🐢🐢🐢🐢🐢🐢🐢
9 | 2.44 ± 0.06 | 2.48 ± 0.06 | 4.92 ± 0.09 | 🚀
10 | 23.6 ± 0.8 | 31.0 ± 2.0 | 55.0 ± 2.0 | 🐢🐢🐢🐢
11 | 19.9 ± 0.2 | 21.4 ± 0.5 | 41.2 ± 0.6 | 🐢🐢🐢🐢
12 | 37.0 ± 3.0 | 600.0 ± 20.0 | 640.0 ± 30.0 | 🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢
13 | 10.0 ± 8.0 | 11.1 ± 0.1 | 21.0 ± 8.0 | 🐢🐢
All days | 109.0 ± 10.0 | 1040.0 ± 20.0 | 1150.0 ± 30.0 | 
<!-- generated table end -->
