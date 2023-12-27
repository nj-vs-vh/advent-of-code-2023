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
1 | $0.613~^{+0.006}_{-0.003}$ | $0.929~^{+0.011}_{-0.005}$ | $1.539~^{+0.012}_{-0.004}$ | 🚀🚀🚀🚀
2 | $1.215~^{+0.062}_{-0.01}$ | $1.37~^{+0.01}_{-0.008}$ | $2.65~^{+1.26}_{-0.06}$ | 🚀🚀🚀
3 | $5.39~^{+0.02}_{-0.03}$ | $4.403~^{+0.011}_{-0.005}$ | $9.8~^{+0.25}_{-0.03}$ | 🚀🚀
4 | $1.029~^{+0.01}_{-0.005}$ | $1.226~^{+0.029}_{-0.004}$ | $2.261~^{+0.059}_{-0.008}$ | 🚀🚀🚀🚀
5 | $0.239~^{+0.009}_{-0.003}$ | $4.261~^{+0.043}_{-0.009}$ | $4.494~^{+0.028}_{-0.009}$ | 🚀🚀🚀
6 | $0.0055~^{+0.0005}_{-0.0005}$ | $0.0~^{+0.0}_{-0.0}$ | $0.0077~^{+0.0004}_{-0.0004}$ | 🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
7 | $3.261~^{+0.057}_{-0.009}$ | $3.441~^{+0.048}_{-0.005}$ | $6.7~^{+0.06}_{-0.01}$ | 🚀🚀
8 | $3.59~^{+0.02}_{-0.05}$ | $336.0~^{+5.0}_{-3.0}$ | $340.0~^{+3.0}_{-2.0}$ | 🐢🐢🐢
9 | $2.36~^{+0.014}_{-0.006}$ | $2.413~^{+0.005}_{-0.005}$ | $4.788~^{+0.009}_{-0.011}$ | 🚀🚀🚀
10 | $23.06~^{+0.05}_{-0.08}$ | $30.36~^{+0.13}_{-0.06}$ | $53.5~^{+0.08}_{-0.16}$ | 🛹
11 | $19.76~^{+0.07}_{-0.02}$ | $21.19~^{+0.09}_{-0.03}$ | $40.97~^{+0.04}_{-0.07}$ | 🛹
12 | $35.6~^{+0.1}_{-0.1}$ | $583.0~^{+9.0}_{-10.0}$ | $628.0~^{+3.0}_{-8.0}$ | 🐢🐢🐢🐢
13 | $8.601~^{+0.016}_{-0.006}$ | $10.912~^{+0.008}_{-0.011}$ | $19.52~^{+0.01}_{-0.02}$ | 🚀
14 | $28.99~^{+0.08}_{-0.05}$ | $3689.7~^{+0.6}_{-5.3}$ | $3718.8~^{+0.8}_{-0.3}$ | 🐢🐢🐢🐢🐢🐢🐢
15 | $1.338~^{+0.003}_{-0.003}$ | $3.51~^{+0.018}_{-0.009}$ | $4.85~^{+0.02}_{-0.01}$ | 🚀🚀🚀
16 | $12.69~^{+0.06}_{-0.07}$ | $2750.0~^{+10.0}_{-40.0}$ | $2778.0~^{+1.0}_{-26.0}$ | 🐢🐢🐢🐢🐢🐢🐢
17 | $498.0~^{+0.7}_{-0.9}$ | $1641.0~^{+9.0}_{-3.0}$ | $2144.0~^{+7.0}_{-7.0}$ | 🐢🐢🐢🐢🐢🐢
18 | $12.03~^{+0.03}_{-0.04}$ | $16.79~^{+0.05}_{-0.02}$ | $28.83~^{+0.08}_{-0.05}$ | 🚀
19 | $2.45~^{+0.03}_{-0.07}$ | $3.73~^{+0.02}_{-0.07}$ | $6.12~^{+0.1}_{-0.05}$ | 🚀🚀
20 | $26.84~^{+0.02}_{-0.02}$ | $291.8~^{+0.1}_{-0.3}$ | $318.6~^{+0.1}_{-0.4}$ | 🐢🐢🐢
21 | $10.13~^{+0.05}_{-0.01}$ | $244.0~^{+0.9}_{-1.1}$ | $254.0~^{+0.8}_{-1.0}$ | 🐢🐢🐢
22 | $419.0~^{+3.0}_{-2.0}$ | $432.3~^{+1.2}_{-0.9}$ | $851.0~^{+6.0}_{-1.0}$ | 🐢🐢🐢🐢🐢
23 | $15.56~^{+0.02}_{-0.04}$ | $14566.3~^{+0.7}_{-1.5}$ | $14581.9~^{+0.7}_{-0.5}$ | 🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢
24 | $41.0~^{+1.7}_{-0.5}$ | $5560.0~^{+20.0}_{-20.0}$ | $5598.0~^{+3.0}_{-32.0}$ | 🐢🐢🐢🐢🐢🐢🐢🐢
25 | $4020.0~^{+20.0}_{-10.0}$ | $0.0~^{+0.0008}_{-0.0}$ | $4040.0~^{+20.0}_{-20.0}$ | 🐢🐢🐢🐢🐢🐢🐢🐢
All days | $5210.0~^{+30.0}_{-30.0}$ | $30179.0~^{+42.0}_{-3.0}$ | $35410.0~^{+20.0}_{-20.0}$ | 
<!-- generated table end -->

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