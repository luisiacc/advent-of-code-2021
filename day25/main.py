#!/usr/bin/env python3.9


def get_input():
    with open("input.txt", "r") as f:
        return [x.strip() for x in f.readlines()]


class Box:
    def __init__(self, grid) -> None:
        self.grid = grid

    def step(self):
        moves = 0
        grid = [x.copy() for x in self.grid]
        R = len(grid)
        C = len(grid[0])
        grid1 = [x.copy() for x in grid]
        for i in range(R):
            for j in range(C):
                cell = grid[i][j]
                nex = (j + 1) % C
                if cell == ">" and grid[i][nex] == ".":
                    grid1[i][nex] = ">"
                    grid1[i][j] = "."
                    moves += 1

        grid2 = [x.copy() for x in grid1]
        for i in range(R):
            for j in range(C):
                cell = grid[i][j]
                nex = (i + 1) % R
                if cell == "v" and grid1[nex][j] == ".":
                    grid2[nex][j] = "v"
                    grid2[i][j] = "."
                    moves += 1

        self.grid = grid2
        return moves


def pg(grid):
    for line in grid:
        for cell in line:
            print(cell, end="")
        print()
    print()


def main():
    box = Box([list(x) for x in get_input()])
    i = 0
    while box.step():
        i += 1
    print(i + 1)


if __name__ == "__main__":
    main()
