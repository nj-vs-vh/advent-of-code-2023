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
1 | 0.61 ± 0.01 | 1.0 ± 0.2 | 1.6 ± 0.2 | 🚀🚀🚀
2 | 1.5 ± 0.7 | 1.5 ± 0.5 | 3.0 ± 1.0 | 🚀🚀
3 | 6.0 ± 0.9 | 5.0 ± 1.0 | 11.0 ± 2.0 | 🛹
4 | 1.05 ± 0.04 | 1.3 ± 0.07 | 2.35 ± 0.09 | 🚀🚀
5 | 0.25 ± 0.02 | 4.35 ± 0.08 | 4.6 ± 0.09 | 🚀
6 | 0.006 ± 0.002 | 0.0022 ± 0.0006 | 0.008 ± 0.003 | 🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
7 | 3.5 ± 0.2 | 3.9 ± 0.8 | 7.4 ± 0.9 | 🚀
8 | 3.7 ± 0.1 | 346.0 ± 6.0 | 350.0 ± 6.0 | 🐢🐢🐢🐢🐢🐢
9 | 2.45 ± 0.08 | 2.5 ± 0.2 | 5.0 ± 0.2 | 🚀
10 | 23.8 ± 0.3 | 31.5 ± 0.5 | 55.3 ± 0.6 | 🐢🐢🐢
11 | 19.8 ± 0.2 | 21.3 ± 0.3 | 41.1 ± 0.4 | 🐢🐢
12 | 38.0 ± 3.0 | 610.0 ± 20.0 | 650.0 ± 30.0 | 🐢🐢🐢🐢🐢🐢🐢
13 | 8.6 ± 0.1 | 10.9 ± 0.1 | 19.6 ± 0.2 | 🐢
14 | 29.0 ± 0.5 | 3670.0 ± 60.0 | 3700.0 ± 60.0 | 🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢
15 | 1.38 ± 0.05 | 3.74 ± 0.09 | 5.1 ± 0.1 | 🚀
All days | 139.0 ± 3.0 | 4720.0 ± 70.0 | 4860.0 ± 70.0 | 
<!-- generated table end -->
