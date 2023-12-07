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
1 | 0.8 ± 0.9 | 1.0 ± 0.3 | 2.0 ± 1.0 | 🛹
2 | 1.3 ± 0.6 | 1.4 ± 0.4 | 2.7 ± 0.8 | 🐢🐢🐢
3 | 5.8 ± 0.4 | 4.7 ± 0.2 | 10.5 ± 0.5 | 🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢
4 | 1.03 ± 0.02 | 1.3 ± 0.2 | 2.3 ± 0.2 | 🐢🐢
5 | 0.25 ± 0.02 | 4.31 ± 0.1 | 4.6 ± 0.1 | 🐢🐢🐢🐢🐢🐢
6 | 0.006 ± 0.001 | 0.0021 ± 0.0009 | 0.008 ± 0.002 | 🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
7 | 3.2 ± 0.1 | 3.7 ± 0.6 | 6.9 ± 0.6 | 🐢🐢🐢🐢🐢🐢🐢🐢
All days | 12.0 ± 1.0 | 16.4 ± 0.9 | 29.0 ± 2.0 | 
<!-- generated table end -->
