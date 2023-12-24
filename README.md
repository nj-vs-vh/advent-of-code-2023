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
1 | 0.8 ± 0.4 | 1.1 ± 0.5 | 1.8 ± 0.6 | 🚀🚀🚀🚀
2 | 1.5 ± 0.8 | 2.0 ± 1.0 | 3.0 ± 1.0 | 🚀🚀🚀
3 | 6.0 ± 1.0 | 4.7 ± 0.8 | 11.0 ± 2.0 | 🚀🚀
4 | 1.05 ± 0.05 | 1.27 ± 0.07 | 2.4 ± 0.1 | 🚀🚀🚀
5 | 0.26 ± 0.02 | 4.42 ± 0.09 | 4.69 ± 0.1 | 🚀🚀🚀
6 | 0.007 ± 0.004 | 0.0022 ± 0.0005 | 0.009 ± 0.003 | 🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
7 | 3.4 ± 0.1 | 3.8 ± 0.7 | 7.3 ± 0.9 | 🚀🚀
8 | 3.58 ± 0.04 | 340.0 ± 3.0 | 344.0 ± 2.0 | 🐢🐢🐢
9 | 2.42 ± 0.07 | 2.46 ± 0.05 | 4.88 ± 0.1 | 🚀🚀🚀
10 | 23.1 ± 0.2 | 30.8 ± 0.3 | 53.9 ± 0.3 | 🛹
11 | 19.9 ± 0.2 | 21.4 ± 0.2 | 41.3 ± 0.3 | 🛹
12 | 36.0 ± 3.0 | 580.0 ± 10.0 | 620.0 ± 10.0 | 🐢🐢🐢🐢
13 | 8.6 ± 0.1 | 10.9 ± 0.1 | 19.5 ± 0.2 | 🚀
14 | 28.9 ± 0.3 | 3450.0 ± 40.0 | 3490.0 ± 50.0 | 🐢🐢🐢🐢🐢🐢🐢
15 | 1.36 ± 0.03 | 3.55 ± 0.04 | 4.92 ± 0.06 | 🚀🚀🚀
16 | 20.0 ± 10.0 | 2780.0 ± 40.0 | 2780.0 ± 40.0 | 🐢🐢🐢🐢🐢🐢🐢
17 | 510.0 ± 20.0 | 1690.0 ± 60.0 | 2210.0 ± 80.0 | 🐢🐢🐢🐢🐢🐢🐢
18 | 14.0 ± 10.0 | 17.4 ± 0.8 | 32.0 ± 10.0 | 🛹
19 | 2.5 ± 0.1 | 10.0 ± 10.0 | 8.0 ± 10.0 | 🚀🚀
20 | 27.4 ± 0.5 | 298.0 ± 2.0 | 325.0 ± 2.0 | 🐢🐢🐢
21 | 10.4 ± 0.2 | 249.0 ± 2.0 | 260.0 ± 1.0 | 🐢🐢🐢
22 | 440.0 ± 20.0 | 450.0 ± 20.0 | 890.0 ± 40.0 | 🐢🐢🐢🐢🐢
23 | 16.2 ± 0.5 | 16220.0 ± 60.0 | 16260.0 ± 50.0 | 🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢
All days | 1180.0 ± 40.0 | 26200.0 ± 100.0 | 27400.0 ± 100.0 | 
<!-- generated table end -->
