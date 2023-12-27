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

Latest results are compiled here:

<!-- generated table start -->
**Day** | **Part 1**, msec | **Part 2**, msec | **Total**, msec | **Relative score**
---: | :---: | :---: | :---: | ---
1 | 0.63 ± 0.06 | 0.94 ± 0.04 | 1.57 ± 0.07 | 🚀🚀🚀🚀
2 | 1.4 ± 0.7 | 1.5 ± 0.5 | 2.9 ± 0.8 | 🚀🚀🚀
3 | 6.0 ± 1.0 | 4.6 ± 0.6 | 10.0 ± 2.0 | 🚀🚀
4 | 1.04 ± 0.03 | 1.25 ± 0.04 | 2.3 ± 0.04 | 🚀🚀🚀🚀
5 | 0.25 ± 0.02 | 4.27 ± 0.08 | 4.53 ± 0.1 | 🚀🚀🚀
6 | 0.006 ± 0.001 | 0.0022 ± 0.0005 | 0.008 ± 0.002 | 🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
7 | 3.29 ± 0.09 | 3.6 ± 0.6 | 7.0 ± 0.7 | 🚀🚀
8 | 3.53 ± 0.03 | 332.5 ± 0.7 | 336.1 ± 0.8 | 🐢🐢🐢
9 | 2.39 ± 0.03 | 2.46 ± 0.06 | 4.85 ± 0.06 | 🚀🚀🚀
10 | 23.3 ± 0.2 | 30.5 ± 0.2 | 53.7 ± 0.2 | 🛹
11 | 19.8 ± 0.1 | 21.5 ± 0.1 | 41.3 ± 0.2 | 🛹
12 | 36.0 ± 3.0 | 580.0 ± 10.0 | 620.0 ± 10.0 | 🐢🐢🐢🐢
13 | 8.6 ± 0.1 | 10.9 ± 0.1 | 19.6 ± 0.2 | 🚀
14 | 28.6 ± 0.4 | 3330.0 ± 40.0 | 3370.0 ± 50.0 | 🐢🐢🐢🐢🐢🐢🐢
15 | 1.34 ± 0.02 | 3.52 ± 0.06 | 4.86 ± 0.06 | 🚀🚀🚀
16 | 10.0 ± 10.0 | 2700.0 ± 30.0 | 2710.0 ± 30.0 | 🐢🐢🐢🐢🐢🐢🐢
17 | 500.0 ± 20.0 | 1680.0 ± 80.0 | 2190.0 ± 60.0 | 🐢🐢🐢🐢🐢🐢
18 | 12.3 ± 0.5 | 19.0 ± 10.0 | 32.0 ± 10.0 | 🚀
19 | 2.5 ± 0.09 | 6.0 ± 10.0 | 6.3 ± 0.2 | 🚀🚀🚀
20 | 27.4 ± 0.6 | 297.0 ± 4.0 | 325.0 ± 4.0 | 🐢🐢🐢
21 | 10.5 ± 0.3 | 250.0 ± 4.0 | 260.0 ± 4.0 | 🐢🐢🐢
22 | 440.0 ± 30.0 | 460.0 ± 30.0 | 890.0 ± 30.0 | 🐢🐢🐢🐢🐢
23 | 30.0 ± 30.0 | 16300.0 ± 100.0 | 16400.0 ± 100.0 | 🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢
24 | 42.2 ± 0.8 | 5670.0 ± 100.0 | 5760.0 ± 90.0 | 🐢🐢🐢🐢🐢🐢🐢🐢
25 | 4180.0 ± 90.0 | 0.0003 ± 0.0005 | 4160.0 ± 90.0 | 🐢🐢🐢🐢🐢🐢🐢🐢
All days | 5420.0 ± 90.0 | 31600.0 ± 100.0 | 37300.0 ± 200.0 | 
<!-- generated table end -->

<details>
<summary>
Reference times at the and of AoC (generated on 26.12.2023)
</summary>
<!-- reference table start -->
**Day** | **Part 1**, msec | **Part 2**, msec | **Total**, msec | **Relative score**
---: | :---: | :---: | :---: | ---
1 | 0.63 ± 0.06 | 0.94 ± 0.04 | 1.57 ± 0.07 | 🚀🚀🚀🚀
2 | 1.4 ± 0.7 | 1.5 ± 0.5 | 2.9 ± 0.8 | 🚀🚀🚀
3 | 6.0 ± 1.0 | 4.6 ± 0.6 | 10.0 ± 2.0 | 🚀🚀
4 | 1.04 ± 0.03 | 1.25 ± 0.04 | 2.3 ± 0.04 | 🚀🚀🚀🚀
5 | 0.25 ± 0.02 | 4.27 ± 0.08 | 4.53 ± 0.1 | 🚀🚀🚀
6 | 0.006 ± 0.001 | 0.0022 ± 0.0005 | 0.008 ± 0.002 | 🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
7 | 3.29 ± 0.09 | 3.6 ± 0.6 | 7.0 ± 0.7 | 🚀🚀
8 | 3.53 ± 0.03 | 332.5 ± 0.7 | 336.1 ± 0.8 | 🐢🐢🐢
9 | 2.39 ± 0.03 | 2.46 ± 0.06 | 4.85 ± 0.06 | 🚀🚀🚀
10 | 23.3 ± 0.2 | 30.5 ± 0.2 | 53.7 ± 0.2 | 🛹
11 | 19.8 ± 0.1 | 21.5 ± 0.1 | 41.3 ± 0.2 | 🛹
12 | 36.0 ± 3.0 | 580.0 ± 10.0 | 620.0 ± 10.0 | 🐢🐢🐢🐢
13 | 8.6 ± 0.1 | 10.9 ± 0.1 | 19.6 ± 0.2 | 🚀
14 | 28.6 ± 0.4 | 3330.0 ± 40.0 | 3370.0 ± 50.0 | 🐢🐢🐢🐢🐢🐢🐢
15 | 1.34 ± 0.02 | 3.52 ± 0.06 | 4.86 ± 0.06 | 🚀🚀🚀
16 | 10.0 ± 10.0 | 2700.0 ± 30.0 | 2710.0 ± 30.0 | 🐢🐢🐢🐢🐢🐢🐢
17 | 500.0 ± 20.0 | 1680.0 ± 80.0 | 2190.0 ± 60.0 | 🐢🐢🐢🐢🐢🐢
18 | 12.3 ± 0.5 | 19.0 ± 10.0 | 32.0 ± 10.0 | 🚀
19 | 2.5 ± 0.09 | 6.0 ± 10.0 | 6.3 ± 0.2 | 🚀🚀🚀
20 | 27.4 ± 0.6 | 297.0 ± 4.0 | 325.0 ± 4.0 | 🐢🐢🐢
21 | 10.5 ± 0.3 | 250.0 ± 4.0 | 260.0 ± 4.0 | 🐢🐢🐢
22 | 440.0 ± 30.0 | 460.0 ± 30.0 | 890.0 ± 30.0 | 🐢🐢🐢🐢🐢
23 | 30.0 ± 30.0 | 16300.0 ± 100.0 | 16400.0 ± 100.0 | 🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢
24 | 42.2 ± 0.8 | 5670.0 ± 100.0 | 5760.0 ± 90.0 | 🐢🐢🐢🐢🐢🐢🐢🐢
25 | 4180.0 ± 90.0 | 0.0003 ± 0.0005 | 4160.0 ± 90.0 | 🐢🐢🐢🐢🐢🐢🐢🐢
All days | 5420.0 ± 90.0 | 31600.0 ± 100.0 | 37300.0 ± 200.0 | 
<!-- reference table end -->
</details>