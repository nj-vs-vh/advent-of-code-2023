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
1 | 0.8 ± 0.4 | 1.3 ± 0.7 | 2.0 ± 1.0 | 🐢🐢
2 | 1.2 ± 0.3 | 1.3 ± 0.2 | 2.5 ± 0.4 | 🐢🐢🐢
3 | 5.4 ± 0.3 | 4.5 ± 0.2 | 9.9 ± 0.4 | 🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢
4 | 1.01 ± 0.02 | 1.3 ± 0.2 | 2.3 ± 0.2 | 🐢🐢🐢
5 | 0.24 ± 0.01 | 4.25 ± 0.05 | 4.5 ± 0.06 | 🐢🐢🐢🐢🐢🐢
6 | 0.006 ± 0.001 | 0.002 ± 0.001 | 0.008 ± 0.002 | 🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
All days | 8.7 ± 0.7 | 12.6 ± 0.9 | 21.0 ± 1.0 | 
<!-- generated table end -->
