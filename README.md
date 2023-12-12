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
1 | 0.7 ± 0.3 | 1.2 ± 0.5 | 1.9 ± 0.7 | 🚀🚀
2 | 1.3 ± 0.5 | 1.5 ± 0.5 | 2.8 ± 0.9 | 🚀🚀
3 | 5.8 ± 0.5 | 4.8 ± 0.3 | 10.7 ± 0.6 | 🐢
4 | 1.08 ± 0.05 | 1.33 ± 0.08 | 2.4 ± 0.1 | 🚀🚀
5 | 0.27 ± 0.03 | 4.7 ± 0.7 | 5.0 ± 0.7 | 🚀
6 | 0.006 ± 0.001 | 0.0021 ± 0.0005 | 0.008 ± 0.002 | 🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
7 | 3.6 ± 0.5 | 3.7 ± 0.5 | 7.3 ± 0.7 | 🛹
8 | 3.6 ± 0.1 | 347.0 ± 7.0 | 350.0 ± 7.0 | 🐢🐢🐢🐢🐢🐢🐢🐢🐢
9 | 2.38 ± 0.04 | 2.42 ± 0.03 | 4.8 ± 0.07 | 🚀
10 | 23.3 ± 0.4 | 30.9 ± 0.6 | 54.2 ± 1.0 | 🐢🐢🐢🐢
11 | 20.0 ± 0.3 | 21.4 ± 0.4 | 41.4 ± 0.5 | 🐢🐢🐢🐢
12 | 37.0 ± 3.0 | 590.0 ± 20.0 | 630.0 ± 20.0 | 🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢
All days | 99.0 ± 3.0 | 1010.0 ± 20.0 | 1110.0 ± 20.0 | 
<!-- generated table end -->
