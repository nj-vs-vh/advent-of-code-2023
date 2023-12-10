# Advent of Code 2023

This year I've decided to pause my attempts to learn Rust and just focus on solving the challenges.
I'm going to use Python, which I know and love, and to make my solutions
- clean
- readable
- fully typed
- reasonably performant

```shell
python run.py <day number> [--debug [--input custom-input.txt [--part 1]]]
```

## Performance measurement

Just for fun, this year I'm keeping track of how long my solutions take to run. Later I might take some time to
optimize them and update the numbers.

Methodology:
- Measured quantity: the time between the moment string input is read from the disk and the moment the answer is calculated
- Averaged over 50 runs
- System: 2021 Mac M1 Pro 16 Gb 

### Results

Updated as days go with `python measure_performance.py`

<!-- generated table start -->
**Day** | **Part 1**, msec | **Part 2**, msec | **Total**, msec | **Relative score**
---: | :---: | :---: | :---: | ---
1 | 0.62 ± 0.04 | 0.95 ± 0.07 | 1.57 ± 0.09 | 🚀🚀
2 | 1.3 ± 0.3 | 1.38 ± 0.09 | 2.6 ± 0.3 | 🚀
3 | 6.0 ± 0.5 | 4.9 ± 0.4 | 10.9 ± 0.6 | 🐢🐢
4 | 1.07 ± 0.05 | 1.31 ± 0.09 | 2.4 ± 0.1 | 🚀
5 | 0.26 ± 0.02 | 4.4 ± 0.1 | 4.6 ± 0.1 | 🛹
6 | 0.006 ± 0.001 | 0.0022 ± 0.0008 | 0.008 ± 0.002 | 🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
7 | 3.6 ± 0.5 | 3.7 ± 0.5 | 7.3 ± 0.7 | 🐢
8 | 3.6 ± 0.09 | 342.0 ± 7.0 | 346.0 ± 7.0 | 🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢
9 | 2.38 ± 0.05 | 2.43 ± 0.05 | 4.81 ± 0.09 | 🛹
10 | 23.2 ± 0.2 | 30.3 ± 0.3 | 53.5 ± 0.4 | 🐢🐢🐢🐢🐢🐢
All days | 42.0 ± 0.7 | 391.0 ± 7.0 | 433.0 ± 7.0 | 
<!-- generated table end -->
