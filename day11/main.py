#!usr/bin/env python3.9
import itertools


def get_input():
    with open("input.txt", "r") as f:
        return [x.strip() for x in f.readlines()]


def neighbors(grid, x, y):
    m = []
    for dx, dy in itertools.product([-1, 0, 1], [-1, 0, 1]):
        X = x + dx
        Y = y + dy
        if (0 <= X < len(grid)) and (0 <= Y < len(grid[0])) and (dx, dy) != (0, 0):
            m.append((X, Y))
    return m


def step(grid):
    f = 0
    flashed: list[tuple] = []

    def flash(x, y):
        nonlocal f
        f += 1
        grid[x][y] = 0
        flashed.append((x, y))
        for xn, yn in neighbors(grid, x, y):
            if (xn, yn) not in flashed:
                grid[xn][yn] += 1
                if grid[xn][yn] > 9:
                    flash(xn, yn)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] += 1

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] > 9 and (i, j) not in flashed:
                flash(i, j)

    return f


def pf(grid):
    for line in grid:
        print("".join(f"({str(x)})" for x in line).replace("0", "-"))
    print()


def main():
    grid = [[int(x) for x in line] for line in get_input()]

    flashes = 0
    for _ in range(100):
        flashes += step(grid)

    print(flashes)


if __name__ == "__main__":
    main()
