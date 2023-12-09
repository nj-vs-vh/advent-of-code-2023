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
1 | 0.9 ± 0.5 | 1.0 ± 1.0 | 2.0 ± 2.0 | 🚀
2 | 2.0 ± 1.0 | 1.5 ± 0.7 | 3.0 ± 2.0 | 🛹
3 | 5.4 ± 0.4 | 4.5 ± 0.2 | 9.9 ± 0.4 | 🐢🐢
4 | 1.03 ± 0.04 | 1.25 ± 0.05 | 2.28 ± 0.08 | 🚀
5 | 0.25 ± 0.02 | 4.28 ± 0.08 | 4.52 ± 0.1 | 🐢
6 | 0.006 ± 0.002 | 0.0021 ± 0.0005 | 0.008 ± 0.002 | 🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
7 | 3.4 ± 0.4 | 3.5 ± 0.3 | 6.9 ± 0.5 | 🐢
8 | 3.57 ± 0.07 | 353.0 ± 6.0 | 356.0 ± 6.0 | 🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢
9 | 2.42 ± 0.05 | 2.47 ± 0.05 | 4.9 ± 0.07 | 🐢
All days | 19.0 ± 1.0 | 372.0 ± 5.0 | 390.0 ± 6.0 | 
<!-- generated table end -->
