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
- Averaged over 100 runs
- System: 2021 Mac M1 Pro 16 Gb 

### Results

Updated as days go with `python measure_performance.py`

<!-- generated table start -->
**Day** | **Part 1**, msec | **Part 2**, msec | **Total**, msec | **Relative score**
---: | :---: | :---: | :---: | ---
1 | 0.7 ± 0.2 | 1.0 ± 0.3 | 1.7 ± 0.4 | 🐢
2 | 1.3 ± 0.4 | 1.35 ± 0.06 | 2.6 ± 0.4 | 🐢🐢🐢
3 | 7.4 ± 0.4 | 6.0 ± 0.5 | 13.4 ± 0.7 | 🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢
4 | 1.04 ± 0.04 | 1.3 ± 0.3 | 2.4 ± 0.3 | 🐢🐢🐢
5 | 0.24 ± 0.01 | 4.3 ± 0.08 | 4.54 ± 0.09 | 🐢🐢🐢🐢🐢
6 | 0.006 ± 0.001 | 0.0021 ± 0.0009 | 0.008 ± 0.002 | 🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
All days | 10.6 ± 0.6 | 14.0 ± 0.6 | 24.6 ± 0.9 | 
<!-- generated table end -->
