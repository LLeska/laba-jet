import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline
from math import pi
from matplotlib.ticker import AutoMinorLocator

# Калибровка ацп
P0 = 215800
P180 = 224244

plt.figure(figsize=(6, 6))
plt.plot([P0, P180], [0, 180], 'blue', linewidth=2, marker='o', markersize=6)
plt.ylabel('Давление, Па', fontsize=14)
plt.xlabel('Показания ацп', fontsize=14)
plt.title('Калибровка ацп', fontsize=14)
ax = plt.gca()
# Автоматические дополнительные деления (4 прxомежуточных деления между основными)
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))

# Основная сетка
plt.grid(True, which='major', linestyle='-', alpha=0.9, linewidth=0.8)
# Дополнительная сетка
plt.grid(True, which='minor', linestyle=':', alpha=0.7, linewidth=0.5)
# Убрал легенду так как только одна линия
# plt.legend(loc='upper left', fontsize=10)
adc = np.array([P0, P180])
P = np.array([0, 180])
k_P, b_P = np.polyfit(adc, P, deg=1)
print((P0 + 100) * k_P + b_P, (P0 - 100) * k_P + b_P)

# Калибровка шаговика
l = np.array([3.35, 3.4, 3.45, 4.45, 4.4])
steps = np.array([600, 600, 600, 800, 800])
k_l, b_l = np.polyfit(steps, l, deg=1)  # deg=1 - линейная аппроксимация

# Создание аппроксимированной прямой
l_fit = k_l * steps + b_l

plt.figure(figsize=(6, 6))
plt.scatter(steps, l, color='blue')
plt.plot(steps, l_fit, 'blue', linewidth=2)
plt.ylabel('Расстояние, см', fontsize=14)
plt.xlabel('Кол-во шагов', fontsize=14)
plt.title('Калибровка Мотора', fontsize=14)
ax = plt.gca()
# Автоматические дополнительные деления (4 промежуточных деления между основными)
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))

# Основная сетка
plt.grid(True, which='major', linestyle='-', alpha=0.9, linewidth=0.8)
# Дополнительная сетка
plt.grid(True, which='minor', linestyle=':', alpha=0.7, linewidth=0.5)
# Убрал легенду так как только одна линия
# plt.legend(loc='upper left', fontsize=10)

files = ["2025-11-19 17_38_16.293858_00мм.csv",
         "2025-11-19 17_41_02.138578_10мм.csv",
         "2025-11-19 17_43_49.242926_20мм.csv",
         "2025-11-19 17_46_04.850486_30мм.csv",
         "2025-11-19 17_48_39.034147_40мм.csv",
         "2025-11-19 17_51_15.608273_50мм.csv",
         "2025-11-19 17_53_14.689181_60мм.csv",
         "2025-11-19 17_55_37.055078_70мм.csv",
         "2025-11-19 17_59_09.888838_80мм.csv",
         "2025-11-19 18_01_39.893790_90мм.csv",
         "2025-11-19 18_05_10.404538_100мм.csv",
         "2025-11-19 18_08_03.905601_110мм.csv"
         ]
P = []
x = []
for i in range(12):
    with open(files[i]) as file:
        P_ = []
        x_ = []
        lines = [line.rstrip() for line in file]
        for i in range(2, 602):
            a, b = map(int, lines[i].split(";"))
            n_ = 0
            if a > 315835: a, n_ = map(int, lines[i - 1].split(";"))
            P_.append(a)
            x_.append(b)
        P.append(P_)
        x.append(sorted(x_))

for i in range(12):
    x[i] = np.array(x[i])
    ind = P[i].index(max(P[i]))
    print(x[i][ind], P[i][ind], max(P[i]))
    x[i] = x[i] * k_l + b_l
    x[i] -= np.float64(x[i][ind])
    ind = P[i].index(max(P[i]))
    print(x[i][ind], P[i][ind], max(P[i]))

# Создаем график
plt.figure(figsize=(6, 6))

colors = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
    '#ff0000', '#000000'
]

for i in range(len(P)):
    P[i] = np.array(P[i])
    P[i] = P[i][100:400]
    x[i] = x[i][100:400]
    P[i] = P[i] * k_P + b_P
    sorted_indices = np.argsort(x[i])
    x[i] = np.array(x[i])[sorted_indices]
    P[i] = P[i][sorted_indices]

    # Удаляем дубликаты и обеспечиваем строгое возрастание x
    # Оставляем только уникальные значения x, усредняя соответствующие y
    unique_x, unique_indices = np.unique(x[i], return_index=True)
    unique_y = np.zeros_like(unique_x)

    for j, ux in enumerate(unique_x):
        mask = x[i] == ux
        unique_y[j] = np.mean(P[i][mask])

    # Создаем сплайн только если есть достаточно точек
    if len(unique_x) > 3:
        cs = CubicSpline(unique_x, unique_y)

        # Гладкие данные для построения
        n = 100
        x[i] = np.linspace(min(x[i]), max(x[i]), n)
        P[i] = cs(x[i])
        P[i] = P[i] - min(P[i])
        ind = np.where(P[i] == max(P[i]))
        x[i] -= x[i][ind]
        plt.plot(x[i], P[i], colors[i], linewidth=2, marker='o', markersize=2, label=f'{i * 10} мм')
    else:
        # Если точек мало, строим простую линейную интерполяцию
        plt.plot(unique_x, unique_y, colors[i], linewidth=2, marker='o', markersize=2, label=f'{i * 10} мм')

# Настраиваем оси и заголовок
plt.xlabel('расстояние от центра сопла, см', fontsize=14)
plt.ylabel('Давление, Па', fontsize=14)
plt.title('Зависимость давления от расстояния до центра сопла\n в разных сечениях', fontsize=12)

ax = plt.gca()
# Автоматические дополнительные деления (4 промежуточных деления между основными)
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))

# Основная сетка
plt.grid(True, which='major', linestyle='-', alpha=0.9, linewidth=0.8)
# Дополнительная сетка
plt.grid(True, which='minor', linestyle=':', alpha=0.7, linewidth=0.5)
plt.legend(loc='best', fontsize=10)
plt.tight_layout()

plt.figure(figsize=(6, 6))

# Предполагаем, что colors уже определен
V = [np.array(p) for p in P]

q = []
for i in range(len(V)):
    V[i] = (np.float64(2/1.2) * V[i]) ** 0.5
    Q = 0

    # Вычисляем расход
    for j in range(len(V[i]) - 1):
        Q += (0.5 * (abs(x[i][j]) * V[i][j] * 0.01 + abs(x[i][j + 1]) * V[i][j + 1] * 0.01) *
              (x[i][j + 1] * 0.01 - x[i][j] * 0.01))
        #if Q == Nan:
        #    pass
    Q = 2 * pi * Q * 1000
    q.append(Q)

    # Строим гладкую кривую
    plt.plot(x[i], V[i],
             color=colors[i % len(colors)],
             linewidth=2,
             label=f'{round(Q, 2)} г/с, {i * 10} мм')

plt.ylabel('Скорость, м/с', fontsize=14)
plt.xlabel('Расстояние от центра сопла, см', fontsize=14)
plt.title('Зависимость скорости от расстояния до центра сопла\n в разных сечениях',
          fontsize=12, pad=20)
ax = plt.gca()

# Автоматические дополнительные деления (4 промежуточных деления между основными)
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))

# Основная сетка
plt.grid(True, which='major', linestyle='-', alpha=0.9, linewidth=0.8)
# Дополнительная сетка
plt.grid(True, which='minor', linestyle=':', alpha=0.7, linewidth=0.5)
plt.legend(loc='best', fontsize=10)

plt.figure(figsize=(6, 6))
plt.plot(list(range(0, 120, 10)), q, 'blue', linewidth=2, marker='o', markersize=6)
plt.ylabel('Массовый расход, г/с', fontsize=14)
plt.xlabel('Расстояния до сопла, мм', fontsize=14)
plt.title('Зависимость массового расхода\n от расстояния до сопла', fontsize=14)
ax = plt.gca()
# Автоматические дополнительные деления (4 промежуточных деления между основными)
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))

# Основная сетка
plt.grid(True, which='major', linestyle='-', alpha=0.9, linewidth=0.8)
# Дополнительная сетка
plt.grid(True, which='minor', linestyle=':', alpha=0.7, linewidth=0.5)
# Убрал легенду так как только одна линия
# plt.legend(loc='upper left', fontsize=10)
plt.tight_layout()

with open("2025-11-19 17_11_55.586047_0Pa.txt") as file:
    P_ = []
    lines = [line.rstrip() for line in file]
    for i in range(2, 502):
        a = int(lines[i])
        if a > 315835: a = int(lines[i - 1])
        P_.append(a)

plt.figure(figsize=(6, 6))
plt.plot(list(range(2, 502)), P_, 'blue', linewidth=2, marker='o', markersize=6)
plt.ylabel('Показания АЦП', fontsize=14)  # Исправил подпись оси
plt.xlabel('Измерения', fontsize=14)  # Исправил подпись оси
plt.title('Зависимость показаний АЦП от времени', fontsize=14)  # Исправил заголовок
ax = plt.gca()
# Автоматические дополнительные деления (4 промежуточных деления между основными)
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))

# Основная сетка
plt.grid(True, which='major', linestyle='-', alpha=0.9, linewidth=0.8)
# Дополнительная сетка
plt.grid(True, which='minor', linestyle=':', alpha=0.7, linewidth=0.5)
# Убрал легенду так как только одна линия
# plt.legend(loc='upper left', fontsize=10)

plt.show()