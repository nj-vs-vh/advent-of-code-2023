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
1 | 0.8 ± 0.6 | 1.2 ± 0.6 | 2.0 ± 1.0 | 🚀🚀
2 | 1.4 ± 0.7 | 1.6 ± 0.8 | 3.0 ± 1.0 | 🚀
3 | 5.5 ± 0.4 | 4.5 ± 0.3 | 10.0 ± 0.5 | 🐢
4 | 1.05 ± 0.03 | 1.27 ± 0.05 | 2.32 ± 0.07 | 🚀🚀
5 | 0.24 ± 0.02 | 4.26 ± 0.07 | 4.51 ± 0.08 | 🚀
6 | 0.006 ± 0.001 | 0.0021 ± 0.0004 | 0.008 ± 0.002 | 🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
7 | 3.4 ± 0.4 | 3.6 ± 0.4 | 7.0 ± 0.6 | 🛹
8 | 3.6 ± 0.1 | 345.0 ± 5.0 | 348.0 ± 5.0 | 🐢🐢🐢🐢🐢🐢🐢
9 | 2.38 ± 0.04 | 2.42 ± 0.04 | 4.8 ± 0.07 | 🚀
10 | 22.9 ± 0.2 | 30.2 ± 0.3 | 53.1 ± 0.5 | 🐢🐢🐢🐢
11 | 791.0 ± 7.0 | 794.0 ± 7.0 | 1580.0 ± 10.0 | 🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢
All days | 832.0 ± 7.0 | 1188.0 ± 7.0 | 2020.0 ± 10.0 | 
<!-- generated table end -->
