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
1 | 0.7 ± 0.3 | 1.0 ± 0.4 | 1.7 ± 0.7 | 🚀🚀🚀
2 | 1.3 ± 0.4 | 1.37 ± 0.04 | 2.7 ± 0.4 | 🚀🚀🚀
3 | 5.5 ± 0.4 | 4.5 ± 0.1 | 10.1 ± 0.4 | 🚀
4 | 1.04 ± 0.03 | 1.26 ± 0.05 | 2.3 ± 0.08 | 🚀🚀🚀
5 | 0.25 ± 0.02 | 4.31 ± 0.07 | 4.55 ± 0.09 | 🚀🚀
6 | 0.006 ± 0.002 | 0.0022 ± 0.0005 | 0.008 ± 0.002 | 🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
7 | 3.28 ± 0.09 | 3.7 ± 0.7 | 6.9 ± 0.7 | 🚀🚀
8 | 3.54 ± 0.02 | 332.5 ± 0.6 | 336.0 ± 0.6 | 🐢🐢🐢🐢🐢
9 | 2.41 ± 0.06 | 2.45 ± 0.06 | 4.9 ± 0.1 | 🚀🚀
10 | 23.3 ± 0.2 | 30.5 ± 0.2 | 53.8 ± 0.4 | 🐢
11 | 20.1 ± 0.1 | 21.5 ± 0.2 | 41.6 ± 0.2 | 🐢
12 | 37.0 ± 3.0 | 610.0 ± 30.0 | 640.0 ± 30.0 | 🐢🐢🐢🐢🐢🐢🐢
13 | 8.7 ± 0.2 | 11.1 ± 0.4 | 19.8 ± 0.5 | 🛹
14 | 29.3 ± 0.4 | 3490.0 ± 50.0 | 3520.0 ± 50.0 | 🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢
15 | 1.35 ± 0.03 | 3.53 ± 0.1 | 4.9 ± 0.1 | 🚀🚀
16 | 10.0 ± 10.0 | 2770.0 ± 60.0 | 2780.0 ± 60.0 | 🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢
17 | 660.0 ± 40.0 | 2200.0 ± 100.0 | 2800.0 ± 200.0 | 🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢
18 | 12.5 ± 0.5 | 20.0 ± 10.0 | 30.0 ± 10.0 | 🛹
19 | 0.0 ± 10.0 | 10.0 ± 10.0 | 10.0 ± 10.0 | 🚀
20 | 27.7 ± 0.5 | 296.3 ± 0.7 | 324.0 ± 1.0 | 🐢🐢🐢🐢🐢
All days | 860.0 ± 50.0 | 9800.0 ± 100.0 | 10600.0 ± 200.0 | 
<!-- generated table end -->
