from matplotlib import pyplot as plt
from math import sqrt
import tabulate
import random


positions = [
    (20, 105),
    (30, 145),
    (45, 99),
    (100, 100),
    (10, 50),
    (10, 20),
    (30, 40),
    (40, 50),
]

distance_matrix = []

for i in range(len(positions)):
    position_x, position_y = positions[i]

    row = []

    for j in range(len(positions)):
        other_x, other_y = positions[j]

        distance = sqrt((position_x - other_x) ** 2 + (position_y - other_y) ** 2)
        row.append(distance)

    distance_matrix.append(row)

print(tabulate.tabulate(distance_matrix))

xs = [x[0] for x in positions]
ys = [y[1] for y in positions]

plt.plot(xs, ys, 'o')
plt.plot(xs, ys)


plt.show()


def ant_colony(position_index, matrix):

    start = positions[position_index]

    pheromone_map = [[0 for _ in range(len(matrix))] for _ in range(len(matrix))]

    current_best = ()

    number_of_virtual_ants = len(matrix)

    while True:

        for i in range(number_of_virtual_ants):
            random.shuffle()
