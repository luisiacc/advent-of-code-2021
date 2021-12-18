#!usr/bin/env python3.9
import itertools
import queue
from collections import Counter, defaultdict, deque


def get_input():
    with open("input.txt", "r") as f:
        return [x.strip() for x in f.readlines()]


o_grid = [[int(x) for x in line] for line in get_input()]


def neigh(grid, i, j):
    m = []
    A = [1, 0, -1, 0]
    B = [0, 1, 0, -1]
    for n in range(4):
        x = A[n]
        y = B[n]
        if 0 <= i + x < len(grid) and 0 <= y + j < len(grid[0]):
            m.append((i + x, j + y))
    return m


def get_min(q, w):
    m = 999999999999
    p = (0, 0)
    for pair in q:
        if w[pair] < m:
            m = w[pair]
            p = pair
    return p


def inc(x, n):
    m = x + n
    if m > 9:
        return m - 9
    return m


def build_big_map(old_grid):
    new_grid = [[0 for _ in range(len(old_grid[0]) * 5)] for __ in range(len(old_grid) * 5)]
    for n in range(5):
        for n1 in range(5):
            for i in range(len(old_grid)):
                for j in range(len(old_grid[0])):
                    new_grid[i + n * len(old_grid)][j + n1 * len(old_grid[0])] = inc(old_grid[i][j], n + n1)
    return new_grid


def main():
    grid = build_big_map(o_grid)
    Q = queue.PriorityQueue()
    Q.put((0, 0, 0))
    W = defaultdict(lambda: 99999999999)
    W[(0, 0)] = 0
    while not Q.empty():
        w, i, j = Q.get()
        for pair in neigh(grid, i, j):
            x, y = pair
            dist = grid[x][y]
            old = W[pair]
            new = W[(i, j)] + dist
            if new < old:
                W[pair] = new
                Q.put((new, x, y))

    print(W[len(grid) - 1, len(grid[0]) - 1] - W[0, 0])

    # for i in range(len(grid)):
    #     for j in range(len(grid[0])):
    #         print(str(W[(i, j)]).zfill(2), end=" ")
    #     print()


if __name__ == "__main__":
    main()
