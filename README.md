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
1 | $0.618~^{+0.0008}_{-0.003}$ | $0.931~^{+0.005}_{-0.001}$ | $1.554~^{+0.002}_{-0.007}$ | 🚀🚀🚀🚀
2 | $1.264~^{+0.057}_{-0.006}$ | $1.409~^{+0.004}_{-0.006}$ | $2.68~^{+0.07}_{-0.01}$ | 🚀🚀🚀
3 | $5.86~^{+0.08}_{-0.09}$ | $4.76~^{+0.05}_{-0.06}$ | $10.64~^{+0.1}_{-0.09}$ | 🚀🚀
4 | $1.04~^{+0.04}_{-0.01}$ | $1.25~^{+0.03}_{-0.01}$ | $2.33~^{+0.02}_{-0.03}$ | 🚀🚀🚀
5 | $0.271~^{+0.003}_{-0.01}$ | $4.48~^{+0.01}_{-0.05}$ | $4.75~^{+0.02}_{-0.05}$ | 🚀🚀🚀
6 | $0.006~^{+0.0002}_{-0.0002}$ | $0.0021~^{+0.0}_{-0.0002}$ | $0.008~^{+0.0001}_{-0.0001}$ | 🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
7 | $3.42~^{+0.04}_{-0.05}$ | $3.58~^{+0.07}_{-0.02}$ | $7.06~^{+0.19}_{-0.05}$ | 🚀🚀
8 | $3.72~^{+0.02}_{-0.01}$ | $351.9~^{+2.5}_{-0.7}$ | $357.4~^{+0.7}_{-1.9}$ | 🐢🐢🐢🐢
9 | $2.59~^{+0.02}_{-0.03}$ | $2.65~^{+0.05}_{-0.05}$ | $5.26~^{+0.04}_{-0.02}$ | 🚀🚀🚀
10 | $24.73~^{+0.24}_{-0.08}$ | $32.8~^{+0.3}_{-0.1}$ | $57.6~^{+0.3}_{-0.2}$ | 🛹
11 | $21.09~^{+0.02}_{-0.06}$ | $22.74~^{+0.07}_{-0.03}$ | $43.8~^{+0.11}_{-0.05}$ | 🛹
12 | $37.1~^{+0.8}_{-0.2}$ | $615.0~^{+6.0}_{-6.0}$ | $654.0~^{+8.0}_{-4.0}$ | 🐢🐢🐢🐢🐢
13 | $9.22~^{+0.04}_{-0.03}$ | $11.75~^{+0.05}_{-0.09}$ | $21.01~^{+0.07}_{-0.06}$ | 🚀
14 | $25.5~^{+0.1}_{-0.2}$ | $2800.0~^{+10.0}_{-100.0}$ | $2760.0~^{+70.0}_{-60.0}$ | 🐢🐢🐢🐢🐢🐢🐢🐢
15 | $1.487~^{+0.036}_{-0.008}$ | $3.84~^{+0.08}_{-0.05}$ | $5.47~^{+0.22}_{-0.09}$ | 🚀🚀
16 | $3.95~^{+0.03}_{-0.01}$ | $810.0~^{+7.0}_{-6.0}$ | $814.0~^{+9.0}_{-4.0}$ | 🐢🐢🐢🐢🐢
17 | $464.0~^{+11.0}_{-2.0}$ | $1600.0~^{+20.0}_{-10.0}$ | $2070.0~^{+80.0}_{-20.0}$ | 🐢🐢🐢🐢🐢🐢🐢
18 | $12.9~^{+0.05}_{-0.04}$ | $18.14~^{+0.06}_{-0.02}$ | $31.02~^{+0.11}_{-0.06}$ | 🚀
19 | $2.56~^{+0.05}_{-0.04}$ | $3.94~^{+0.05}_{-0.03}$ | $6.54~^{+0.08}_{-0.07}$ | 🚀
20 | $29.71~^{+0.05}_{-0.03}$ | $319.2~^{+0.1}_{-0.2}$ | $349.0~^{+0.2}_{-0.3}$ | 🐢🐢🐢🐢
21 | $11.15~^{+0.11}_{-0.02}$ | $268.6~^{+1.4}_{-0.4}$ | $280.3~^{+2.1}_{-0.6}$ | 🐢🐢🐢
22 | $385.0~^{+5.0}_{-4.0}$ | $393.0~^{+5.0}_{-6.0}$ | $790.0~^{+30.0}_{-20.0}$ | 🐢🐢🐢🐢🐢
23 | $17.37~^{+0.1}_{-0.16}$ | $10453.0~^{+7.0}_{-3.0}$ | $10480.0~^{+51.0}_{-9.0}$ | 🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢
24 | $43.2~^{+0.2}_{-0.2}$ | $267.0~^{+4.0}_{-8.0}$ | $314.0~^{+3.0}_{-9.0}$ | 🐢🐢🐢
25 | $208.0~^{+36.0}_{-7.0}$ | $0.001~^{+0.0}_{-0.001}$ | $200.0~^{+30.0}_{-20.0}$ | 🐢🐢🐢
All days | $1350.0~^{+30.0}_{-10.0}$ | $17970.0~^{+50.0}_{-20.0}$ | $19370.0~^{+40.0}_{-40.0}$ | 
<!-- generated table end -->

Notes:
- My code for day 25 is Monte Carlo based, i.e. it has a certain probability of not finding a solution. This leads to a tradeoff where performance could be technically increased at the cost of reduced success probability. The presented performance corresponds to a success rate of around 75%.

<details>
<summary>
Reference times at the and of AoC (generated on 26.12.2023)
</summary>

<!-- reference table start -->
**Day** | **Part 1**, msec | **Part 2**, msec | **Total**, msec | **Relative score**
---: | :---: | :---: | :---: | ---
1 | $0.806~^{+0.004}_{-0.002}$ | $1.109~^{+0.006}_{-0.003}$ | $1.648~^{+0.009}_{-0.002}$ | 🚀🚀🚀🚀
2 | $1.453~^{+0.053}_{-0.004}$ | $2.0~^{+0.01}_{-0.01}$ | $3.71~^{+0.08}_{-0.01}$ | 🚀🚀🚀
3 | $5.41~^{+0.2}_{-0.03}$ | $4.462~^{+0.063}_{-0.009}$ | $10.0~^{+0.1}_{-0.2}$ | 🚀🚀
4 | $1.028~^{+0.009}_{-0.005}$ | $1.24~^{+0.016}_{-0.006}$ | $2.26~^{+0.01}_{-0.02}$ | 🚀🚀🚀🚀
5 | $0.2497~^{+0.0028}_{-0.0002}$ | $4.265~^{+0.019}_{-0.009}$ | $4.494~^{+0.018}_{-0.005}$ | 🚀🚀🚀
6 | $0.006~^{+0.0}_{-0.0007}$ | $0.0021~^{+0.0002}_{-0.0}$ | $0.008~^{+0.0002}_{-0.0006}$ | 🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
7 | $3.3~^{+0.05}_{-0.02}$ | $3.69~^{+0.08}_{-0.04}$ | $7.16~^{+0.09}_{-0.07}$ | 🚀🚀
8 | $3.559~^{+0.019}_{-0.005}$ | $334.6~^{+2.1}_{-0.7}$ | $337.3~^{+1.5}_{-0.8}$ | 🐢🐢🐢
9 | $2.43~^{+0.03}_{-0.02}$ | $2.47~^{+0.03}_{-0.03}$ | $4.91~^{+0.02}_{-0.04}$ | 🚀🚀🚀
10 | $24.2~^{+0.2}_{-0.2}$ | $31.4~^{+0.3}_{-0.2}$ | $55.4~^{+0.6}_{-0.5}$ | 🛹
11 | $20.25~^{+0.08}_{-0.11}$ | $22.0~^{+0.2}_{-0.2}$ | $42.5~^{+0.2}_{-0.3}$ | 🛹
12 | $37.5~^{+0.7}_{-1.0}$ | $620.0~^{+10.0}_{-20.0}$ | $664.0~^{+14.0}_{-10.0}$ | 🐢🐢🐢🐢
13 | $8.692~^{+0.035}_{-0.01}$ | $11.0~^{+0.03}_{-0.04}$ | $19.7~^{+0.13}_{-0.03}$ | 🚀
14 | $29.6~^{+0.6}_{-0.1}$ | $3710.0~^{+20.0}_{-70.0}$ | $3750.0~^{+20.0}_{-100.0}$ | 🐢🐢🐢🐢🐢🐢🐢
15 | $1.39~^{+0.02}_{-0.03}$ | $3.62~^{+0.05}_{-0.12}$ | $4.98~^{+0.08}_{-0.07}$ | 🚀🚀🚀
16 | $15.4~^{+0.3}_{-0.1}$ | $2760.0~^{+30.0}_{-20.0}$ | $2780.0~^{+30.0}_{-10.0}$ | 🐢🐢🐢🐢🐢🐢🐢
17 | $560.0~^{+20.0}_{-20.0}$ | $1866.0~^{+9.0}_{-41.0}$ | $2430.0~^{+40.0}_{-90.0}$ | 🐢🐢🐢🐢🐢🐢🐢
18 | $14.17~^{+0.04}_{-0.04}$ | $17.37~^{+0.03}_{-0.04}$ | $31.62~^{+0.03}_{-0.08}$ | 🚀
19 | $6.13~^{+0.06}_{-0.07}$ | $3.79~^{+0.07}_{-0.05}$ | $6.26~^{+0.09}_{-0.06}$ | 🚀🚀🚀
20 | $27.39~^{+0.11}_{-0.05}$ | $296.4~^{+1.7}_{-0.3}$ | $323.7~^{+1.9}_{-0.4}$ | 🐢🐢🐢
21 | $10.42~^{+0.09}_{-0.06}$ | $250.0~^{+2.3}_{-1.0}$ | $261.0~^{+2.0}_{-2.0}$ | 🐢🐢🐢
22 | $435.0~^{+8.0}_{-6.0}$ | $455.0~^{+9.0}_{-6.0}$ | $880.0~^{+13.0}_{-6.0}$ | 🐢🐢🐢🐢🐢
23 | $16.9~^{+0.2}_{-0.2}$ | $16500.0~^{+100.0}_{-100.0}$ | $16550.0~^{+20.0}_{-30.0}$ | 🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢
24 | $42.72~^{+0.14}_{-0.03}$ | $5750.0~^{+70.0}_{-30.0}$ | $5660.0~^{+70.0}_{-20.0}$ | 🐢🐢🐢🐢🐢🐢🐢🐢
25 | $4118.0~^{+7.0}_{-114.0}$ | $0.0005~^{+0.001}_{-0.0}$ | $4138.0~^{+5.0}_{-3.0}$ | 🐢🐢🐢🐢🐢🐢🐢🐢
All days | $5390.0~^{+20.0}_{-70.0}$ | $32410.0~^{+100.0}_{-240.0}$ | $37400.0~^{+100.0}_{-1200.0}$ | 
<!-- reference table end -->

</details>