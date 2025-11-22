import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline
from math import pi

# Калибровка ацп
P0 = 215800
P180 = 224244

plt.figure(figsize=(10, 6))
plt.plot([P0, P180], [0, 180], 'blue', linewidth=2, marker='o', markersize=6)
plt.ylabel('Давление, Па', fontsize=12)
plt.xlabel('Показания ацп', fontsize=12)
plt.title('Калибровка ацп', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(loc='upper left', fontsize=10)
# plt.tight_layout()
adc = np.array([P0, P180])
P = np.array([0, 180])
k_P, b_P = np.polyfit(adc, P, deg=1)

# Калибровка шаговика
l = np.array([3.35, 3.4, 3.45, 4.45, 4.4])
steps = np.array([600, 600, 600, 800, 800])
k_l, b_l = np.polyfit(steps, l, deg=1)  # deg=1 - линейная аппроксимация

# Создание аппроксимированной прямой
l_fit = k_l * steps + b_l

plt.figure(figsize=(10, 6))
plt.scatter(steps, l, color='blue')
plt.plot(steps, l_fit, 'blue', linewidth=2)
plt.ylabel('Расстояние, см', fontsize=12)
plt.xlabel('Кол-во шагов', fontsize=12)
plt.title('Калибровка Мотора', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(loc='upper left', fontsize=10)
# plt.tight_layout()
with open("2025-11-19 17_38_16.293858_00мм.csv") as file:
    x = []
    P00 = []
    lines = [line.rstrip() for line in file]
    for i in range(2, 602):
        a, b = map(int, lines[i].split(";"))
        x.append(b)
        if a > 315835: a, b = map(int, lines[i - 1].split(";"))
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

P = [P00, P10, P20, P30, P40, P50, P60, P70, P80, P90, P100, P110]
for i in range(len(P)):
    P[i] = np.array(P[i])
    P[i] = P[i] * k_P + b_P
    P[i] = P[i] - min(P[i])
    sorted_indices = np.argsort(x)
    x_sorted = np.array(x)[sorted_indices]
    y_sorted = P[i][sorted_indices]

    # Создаем сплайн
    cs = CubicSpline(x_sorted, y_sorted)

    # Гладкие данные для построения
    n = 100
    x_smooth = np.linspace(min(x), max(x), n)
    y_smooth = cs(x_smooth)
    plt.plot(x_smooth, y_smooth, colors[i], linewidth=2, marker='o', markersize=2, label=f'{i * 10} мм')

# Настраиваем оси и заголовок
plt.xlabel('расстояние от центра сопла, см', fontsize=12)
plt.ylabel('Давление, Па', fontsize=12)
plt.title('Зависимость давления от расстояния до центра сопла в разных сечениях', fontsize=14)

plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(loc='upper left', fontsize=10)

plt.figure(figsize=(12, 8))

# Предполагаем, что colors уже определен
V = [np.array(p) for p in P]

for i in range(len(V)):
    V[i] = (2 * V[i] / 1.2) ** 0.5
    Q = 0
    # Создаем гладкую кривую с помощью кубического сплайна
    # Сортируем по x для корректной интерполяции
    sorted_indices = np.argsort(x)
    x_sorted = np.array(x)[sorted_indices]
    y_sorted = V[i][sorted_indices]

    # Создаем сплайн
    cs = CubicSpline(x_sorted, y_sorted)

    # Гладкие данные для построения
    n = 100
    x_smooth = np.linspace(min(x), max(x), n)
    y_smooth = cs(x_smooth)
    for j in range(len(y_smooth) - 1):
        Q += 0.5 * (x[j * (600 // n)] * y_smooth[j] * 0.01 + x[(j + 1) * (600 // n)] * y_smooth[j + 1] * 0.01) * (
                    x[(j + 1) * (600 // n)] * 0.01 - x[j * (600 // n)] * 0.01)
    Q = 2 * pi * Q * 1000
    # Строим гладкую кривую
    plt.plot(x_smooth, y_smooth,
             color=colors[i % len(colors)],
             linewidth=2,
             label=f'{round(Q, 2)} г/с')

    # Исходные точки
    # plt.scatter(x, P_modified[i], color=colors[i % len(colors)], s=6, zorder=1)

plt.xlabel('Скорость, м/с', fontsize=14)
plt.ylabel('Расстояние от центра сопла, см', fontsize=14)
plt.title('Зависимость скорости от расстояния до центра сопла в разных сечениях',
          fontsize=16, pad=20)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(loc='best', fontsize=10)
plt.tight_layout()

plt.show()
