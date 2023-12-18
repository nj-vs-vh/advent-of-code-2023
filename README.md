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
1 | 0.8 ± 0.4 | 1.2 ± 0.6 | 2.0 ± 1.0 | 🚀🚀🚀
2 | 1.4 ± 0.6 | 2.0 ± 4.0 | 4.0 ± 4.0 | 🚀🚀
3 | 5.5 ± 0.4 | 4.6 ± 0.1 | 10.1 ± 0.4 | 🚀
4 | 1.04 ± 0.03 | 1.24 ± 0.03 | 2.28 ± 0.06 | 🚀🚀🚀
5 | 0.25 ± 0.02 | 4.36 ± 0.06 | 4.61 ± 0.07 | 🚀🚀
6 | 0.006 ± 0.002 | 0.0021 ± 0.0005 | 0.008 ± 0.002 | 🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
7 | 3.31 ± 0.09 | 3.7 ± 0.6 | 7.0 ± 0.7 | 🚀🚀
8 | 3.59 ± 0.08 | 369.0 ± 7.0 | 373.0 ± 7.0 | 🐢🐢🐢🐢🐢
9 | 2.39 ± 0.06 | 2.44 ± 0.05 | 4.83 ± 0.1 | 🚀🚀
10 | 23.8 ± 1.0 | 31.0 ± 1.0 | 55.0 ± 2.0 | 🐢🐢
11 | 20.2 ± 0.3 | 21.8 ± 0.4 | 41.9 ± 0.7 | 🐢
12 | 38.0 ± 4.0 | 620.0 ± 30.0 | 650.0 ± 30.0 | 🐢🐢🐢🐢🐢🐢🐢
13 | 8.6 ± 0.1 | 10.9 ± 0.2 | 19.5 ± 0.3 | 🛹
14 | 29.1 ± 0.3 | 3650.0 ± 50.0 | 3680.0 ± 50.0 | 🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢
15 | 1.35 ± 0.04 | 3.5 ± 0.08 | 4.8 ± 0.1 | 🚀🚀
16 | 10.0 ± 10.0 | 2740.0 ± 50.0 | 2750.0 ± 50.0 | 🐢🐢🐢🐢🐢🐢🐢🐢🐢
17 | 530.0 ± 40.0 | 1800.0 ± 100.0 | 2300.0 ± 200.0 | 🐢🐢🐢🐢🐢🐢🐢🐢🐢
18 | 12.3 ± 0.6 | 19.0 ± 10.0 | 31.0 ± 10.0 | 🐢
All days | 690.0 ± 40.0 | 9200.0 ± 200.0 | 9900.0 ± 200.0 | 
<!-- generated table end -->
