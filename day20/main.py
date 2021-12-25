#!usr/bin/env python3.9

import itertools
import math
import sys
from collections import Counter, defaultdict, deque
from typing import Optional

sys.setrecursionlimit(9999999)


def get_input():
    with open("sample.txt", "r") as f:
        return [x.strip() for x in f.readlines()]


algorithm = get_input()[0]
grid = get_input()[2:]

m = {
    ".": 0,
    "#": 1,
}

grid = [[m[x] for x in line] for line in grid]


def get_output(grid, x, y):
    code = ""
    for (i, j) in itertools.product((-1, 0, 1), (-1, 0, 1)):
        if 0 <= x + i < len(grid) and 0 <= y + j < len(grid[0]):
            code += str(grid[x + i][y + j])
        else:
            code += "0"
    code_number = int(code, 2)
    position_in_algorithm = algorithm[code_number]
    result = m[position_in_algorithm]
    # print(x, y, "->", position_in_algorithm, code)
    return result


light_points = []
for _ in range(2):
    light_points = [(i, j) for i, line in enumerate(grid) for j, _ in enumerate(line) if x == 1]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            output_grid[i][j] = get_output(grid, i, j)

    grid = output_grid

# n = {
#     0: ".",
#     1: "#",
# }
# for i in range(len(grid)):
#     for j in range(len(grid[0])):
#         print(n[grid[i][j]], end="")
#     print()

print(sum(line.count(1) for line in grid))
