#!usr/bin/env python3.9
import itertools
from collections import Counter, defaultdict, deque


def get_input():
    with open("input.txt", "r") as f:
        return [x.strip() for x in f.readlines()]


grid = [[int(x) for x in line] for line in get_input()]


def neigh(i, j):
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


def main():

    V = []
    Q = [(0, 0)]
    W = defaultdict(lambda: 99999999999)
    W[(0, 0)] = grid[0][0]
    V = []
    while Q:
        i, j = get_min(Q, W)
        Q.remove((i, j))
        w = W[(i, j)]
        V.append((i, j))
        for pair in neigh(i, j):
            x, y = pair
            if pair not in V and W[pair] > w + grid[x][y]:
                W[pair] = w + grid[x][y]
                Q.append(pair)

    point = len(grid) - 1, len(grid[0]) - 1
    c = 0
    while point != (0, 0):
        min_neighbor = min(neigh(*point), key=lambda p: W[p])
        c += W[point] - W[min_neighbor]
        point = min_neighbor
    print(c)

    # for i in range(len(grid)):
    #     for j in range(len(grid[0])):
    #         print(str(W[(i, j)]).zfill(2), end=" ")
    #     print()


if __name__ == "__main__":
    main()
