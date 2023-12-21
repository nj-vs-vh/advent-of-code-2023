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
1 | 0.7 ± 0.1 | 1.1 ± 0.5 | 1.8 ± 0.5 | 🚀🚀🚀
2 | 2.0 ± 2.0 | 1.6 ± 0.7 | 3.0 ± 2.0 | 🚀🚀🚀
3 | 5.8 ± 0.4 | 4.8 ± 0.2 | 10.5 ± 0.5 | 🚀
4 | 1.08 ± 0.07 | 1.31 ± 0.07 | 2.4 ± 0.1 | 🚀🚀🚀
5 | 0.26 ± 0.02 | 4.4 ± 0.1 | 4.7 ± 0.2 | 🚀🚀
6 | 0.006 ± 0.002 | 0.0022 ± 0.0006 | 0.008 ± 0.003 | 🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
7 | 3.5 ± 0.2 | 4.0 ± 0.8 | 7.5 ± 0.8 | 🚀🚀
8 | 3.7 ± 0.2 | 349.4 ± 0.9 | 353.1 ± 0.9 | 🐢🐢🐢🐢🐢
9 | 2.48 ± 0.09 | 2.51 ± 0.08 | 5.0 ± 0.1 | 🚀🚀
10 | 23.8 ± 0.2 | 31.7 ± 0.4 | 55.5 ± 0.5 | 🐢
11 | 20.4 ± 0.3 | 22.3 ± 0.2 | 42.7 ± 0.3 | 🐢
12 | 39.0 ± 3.0 | 650.0 ± 10.0 | 690.0 ± 20.0 | 🐢🐢🐢🐢🐢🐢
13 | 8.9 ± 0.2 | 11.3 ± 0.1 | 20.2 ± 0.2 | 🛹
14 | 31.0 ± 1.0 | 3910.0 ± 30.0 | 3940.0 ± 30.0 | 🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢
15 | 1.4 ± 0.04 | 3.68 ± 0.09 | 5.1 ± 0.1 | 🚀🚀
16 | 20.0 ± 10.0 | 2880.0 ± 30.0 | 2890.0 ± 30.0 | 🐢🐢🐢🐢🐢🐢🐢🐢🐢
17 | 615.0 ± 5.0 | 2200.0 ± 400.0 | 2800.0 ± 400.0 | 🐢🐢🐢🐢🐢🐢🐢🐢🐢
18 | 13.2 ± 0.8 | 20.0 ± 10.0 | 30.0 ± 10.0 | 🛹
19 | 0.0 ± 10.0 | 10.0 ± 10.0 | 10.0 ± 10.0 | 🚀
20 | 28.4 ± 0.5 | 302.4 ± 0.5 | 330.8 ± 0.8 | 🐢🐢🐢🐢🐢
21 | 11.0 ± 0.3 | 261.0 ± 1.0 | 272.0 ± 1.0 | 🐢🐢🐢🐢🐢
All days | 830.0 ± 20.0 | 10600.0 ± 300.0 | 11500.0 ± 300.0 | 
<!-- generated table end -->
