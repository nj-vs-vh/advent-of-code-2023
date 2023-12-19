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
1 | 0.7 ± 0.4 | 1.2 ± 0.8 | 1.9 ± 0.9 | 🚀🚀🚀
2 | 1.6 ± 0.8 | 2.0 ± 2.0 | 4.0 ± 2.0 | 🚀🚀
3 | 5.6 ± 0.6 | 4.7 ± 0.7 | 10.0 ± 1.0 | 🚀
4 | 1.08 ± 0.05 | 1.4 ± 0.3 | 2.4 ± 0.3 | 🚀🚀🚀
5 | 0.26 ± 0.02 | 4.3 ± 0.1 | 4.6 ± 0.1 | 🚀🚀
6 | 0.006 ± 0.002 | 0.0021 ± 0.0005 | 0.008 ± 0.002 | 🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
7 | 3.4 ± 0.1 | 3.8 ± 0.7 | 7.2 ± 0.8 | 🚀
8 | 3.63 ± 0.07 | 344.0 ± 4.0 | 348.0 ± 4.0 | 🐢🐢🐢🐢🐢
9 | 2.43 ± 0.05 | 2.48 ± 0.05 | 4.91 ± 0.09 | 🚀🚀
10 | 23.8 ± 0.2 | 31.5 ± 0.3 | 55.2 ± 0.4 | 🐢🐢
11 | 20.2 ± 0.1 | 21.7 ± 0.2 | 41.9 ± 0.2 | 🐢
12 | 39.0 ± 4.0 | 630.0 ± 20.0 | 670.0 ± 20.0 | 🐢🐢🐢🐢🐢🐢🐢
13 | 9.0 ± 0.2 | 11.5 ± 0.3 | 20.5 ± 0.4 | 🛹
14 | 29.9 ± 0.3 | 3870.0 ± 50.0 | 3900.0 ± 50.0 | 🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢
15 | 1.38 ± 0.03 | 3.7 ± 0.06 | 5.08 ± 0.08 | 🚀🚀
16 | 20.0 ± 10.0 | 2820.0 ± 60.0 | 2830.0 ± 50.0 | 🐢🐢🐢🐢🐢🐢🐢🐢🐢
17 | 580.0 ± 20.0 | 2010.0 ± 60.0 | 2600.0 ± 80.0 | 🐢🐢🐢🐢🐢🐢🐢🐢🐢
18 | 12.8 ± 0.5 | 20.0 ± 10.0 | 30.0 ± 10.0 | 🐢
19 | 0.0 ± 10.0 | 10.0 ± 10.0 | 10.0 ± 10.0 | 🚀
All days | 760.0 ± 30.0 | 9800.0 ± 100.0 | 10500.0 ± 100.0 | 
<!-- generated table end -->
