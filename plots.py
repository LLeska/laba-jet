import matplotlib.pyplot as plt
import numpy as np


#Калибровка ацп
P0 = 215800
P180 = 224244

plt.figure(figsize=(10, 6))
plt.plot([P0, P180], [0, 180], 'blue', linewidth=2, marker='o', markersize=6)
plt.ylabel('Давление, Па', fontsize=12)
plt.xlabel('Показания ацп', fontsize=12)
plt.title('Калибровка ацп', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(loc='upper left', fontsize=10)
#plt.tight_layout()
adc = np.array([P0, P180])
P = np.array([0, 180])
k_P, b_P = np.polyfit(adc, P, deg=1)

#Калибровка шаговика
l = np.array([3.35, 3.4, 3.45, 4.45, 4.4])
steps = np.array([600, 600, 600, 800, 800])
k_l, b_l = np.polyfit(steps, l, deg=1)  # deg=1 - линейная аппроксимация

# Создание аппроксимированной прямой
l_fit = k_l * steps + b_l

plt.figure(figsize=(10, 6))
plt.scatter(steps, l, color='blue')
plt.plot( steps, l_fit, 'blue', linewidth=2)
plt.ylabel('Расстояние, см', fontsize=12)
plt.xlabel('Кол-во шагов', fontsize=12)
plt.title('Калибровка Мотора', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(loc='upper left', fontsize=10)
#plt.tight_layout()
with open("2025-11-19 17_38_16.293858_00мм.csv") as file:
    x = []
    P00 = []
    lines = [line.rstrip() for line in file]
    for i in range(2, 602):
        a, b = map(int, lines[i].split(";"))
        x.append(b)
        if a > 315835 : a, b = map(int, lines[i-1].split(";"))
        P00.append(a)
with open("2025-11-19 17_41_02.138578_10мм.csv") as file:
    P10 = []
    lines = [line.rstrip() for line in file]
    for i in range(2, 602):
        a, b = map(int, lines[i].split(";"))
        if a > 315835: a, b = map(int, lines[i - 1].split(";"))
        P10.append(a)
with open("2025-11-19 17_43_49.242926_20мм.csv") as file:
    P20 = []
    lines = [line.rstrip() for line in file]
    for i in range(2, 602):
        a, b = map(int, lines[i].split(";"))
        if a > 315835: a, b = map(int, lines[i - 1].split(";"))
        P20.append(a)
with open("2025-11-19 17_46_04.850486_30мм.csv") as file:
    P30 = []
    lines = [line.rstrip() for line in file]
    for i in range(2, 602):
        a, b = map(int, lines[i].split(";"))
        if a > 315835: a, b = map(int, lines[i - 1].split(";"))
        P30.append(a)
with open("2025-11-19 17_48_39.034147_40мм.csv") as file:
    P40 = []
    lines = [line.rstrip() for line in file]
    for i in range(2, 602):
        a, b = map(int, lines[i].split(";"))
        if a > 315835: a, b = map(int, lines[i - 1].split(";"))
        P40.append(a)
with open("2025-11-19 17_51_15.608273_50мм.csv") as file:
    P50 = []
    lines = [line.rstrip() for line in file]
    for i in range(2, 602):
        a, b = map(int, lines[i].split(";"))
        if a > 315835: a, b = map(int, lines[i - 1].split(";"))
        P50.append(a)
with open("2025-11-19 17_53_14.689181_60мм.csv") as file:
    P60 = []
    lines = [line.rstrip() for line in file]
    for i in range(2, 602):
        a, b = map(int, lines[i].split(";"))
        if a > 315835: a, b = map(int, lines[i - 1].split(";"))
        P60.append(a)
with open("2025-11-19 17_55_37.055078_70мм.csv") as file:
    P70 = []
    lines = [line.rstrip() for line in file]
    for i in range(2, 602):
        a, b = map(int, lines[i].split(";"))
        if a > 315835: a, b = map(int, lines[i - 1].split(";"))
        P70.append(a)
with open("2025-11-19 17_59_09.888838_80мм.csv") as file:
    P80 = []
    lines = [line.rstrip() for line in file]
    for i in range(2, 602):
        a, b = map(int, lines[i].split(";"))
        if a > 315835: a, b = map(int, lines[i - 1].split(";"))
        P80.append(a)
with open("2025-11-19 18_01_39.893790_90мм.csv") as file:
    P90 = []
    lines = [line.rstrip() for line in file]
    for i in range(2, 602):
        a, b = map(int, lines[i].split(";"))
        if a > 315835: a, b = map(int, lines[i - 1].split(";"))
        P90.append(a)
with open("2025-11-19 18_05_10.404538_100мм.csv") as file:
    P100 = []
    lines = [line.rstrip() for line in file]
    for i in range(2, 602):
        a, b = map(int, lines[i].split(";"))
        if a > 315835: a, b = map(int, lines[i - 1].split(";"))
        P100.append(a)
with open("2025-11-19 18_08_03.905601_110мм.csv") as file:
    P110 = []
    lines = [line.rstrip() for line in file]
    for i in range(2, 602):
        a, b = map(int, lines[i].split(";"))
        if a > 315835: a, b = map(int, lines[i - 1].split(";"))
        P110.append(a)

x = np.array(x)
b_l += 0.15
x = x * k_l + b_l


# Создаем график
plt.figure(figsize=(10, 6))

colors = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
    '#ff0000', '#000000'
]
P00 = np.array(P00)
P00 = P00*k_P + b_P
P10 = np.array(P10)
P10 = P10*k_P + b_P
P20 = np.array(P20)
P20 = P20*k_P + b_P
P30 = np.array(P30)
P30 = P30*k_P + b_P
P40 = np.array(P40)
P40 = P40*k_P + b_P
P50 = np.array(P50)
P50 = P50*k_P + b_P
P60 = np.array(P60)
P60 = P60*k_P + b_P
P70 = np.array(P70)
P70 = P70*k_P + b_P
P80 = np.array(P80)
P80 = P80*k_P + b_P
P90 = np.array(P90)
P90 = P90*k_P + b_P
P100 = np.array(P100)
P100 = P100*k_P + b_P
P110 = np.array(P110)
P110 = P110*k_P + b_P


# Рисуем три кривые с разными стилями
plt.plot(x, P00, colors[0], linewidth=2, marker='o', markersize=2, label='0 мм')
plt.plot(x, P10, colors[1], linewidth=2, marker='o', markersize=2, label='10 мм')
plt.plot(x, P20, colors[2], linewidth=2, marker='o', markersize=2, label='20 мм')
plt.plot(x, P30, colors[3], linewidth=2, marker='o', markersize=2, label='30 мм')
plt.plot(x, P40, colors[4], linewidth=2, marker='o', markersize=2, label='40 мм')
plt.plot(x, P50, colors[5], linewidth=2, marker='o', markersize=2, label='50 мм')
plt.plot(x, P60, colors[6], linewidth=2, marker='o', markersize=2, label='60 мм')
plt.plot(x, P70, colors[7], linewidth=2, marker='o', markersize=2, label='70 мм')
plt.plot(x, P80, colors[8], linewidth=2, marker='o', markersize=2, label='80 мм')
plt.plot(x, P90, colors[9], linewidth=2, marker='o', markersize=2, label='90 мм')
plt.plot(x, P100, colors[10], linewidth=2, marker='o', markersize=2, label='100 мм')
plt.plot(x, P110, colors[11], linewidth=2, marker='o', markersize=2, label='110 мм')




# Настраиваем оси и заголовок
plt.xlabel('расстояние от центра сопла', fontsize=12)
plt.ylabel('Давление', fontsize=12)
plt.title('Зависимость давления от расстояния до центра сопла в разных сечениях', fontsize=14)

plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(loc='upper left', fontsize=10)


plt.tight_layout()


plt.show()