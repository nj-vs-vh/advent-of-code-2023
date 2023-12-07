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
1 | 0.7 ± 0.3 | 1.0 ± 0.5 | 1.7 ± 0.7 | 🛹
2 | 1.3 ± 0.4 | 1.3 ± 0.4 | 2.6 ± 0.7 | 🐢🐢🐢
3 | 5.4 ± 0.3 | 4.5 ± 0.2 | 9.9 ± 0.3 | 🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢
4 | 1.02 ± 0.03 | 1.3 ± 0.3 | 2.3 ± 0.3 | 🐢🐢
5 | 0.24 ± 0.02 | 4.22 ± 0.05 | 4.46 ± 0.06 | 🐢🐢🐢🐢🐢🐢
6 | 0.006 ± 0.001 | 0.0021 ± 0.0008 | 0.008 ± 0.002 | 🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
7 | 3.4 ± 0.4 | 3.5 ± 0.4 | 6.9 ± 0.5 | 🐢🐢🐢🐢🐢🐢🐢🐢
All days | 12.0 ± 0.7 | 15.9 ± 0.8 | 28.0 ± 1.0 | 
<!-- generated table end -->
