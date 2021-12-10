#!usr/bin/env python3.9
def get_input():
    with open("input.txt", "r") as f:
        return [x.strip() for x in f.readlines()]


vertical = (1, 0, -1, 0)
horizontal = (0, 1, 0, -1)

cache = []


def find_basin(area, i, j):
    b = 1
    if (i, j) in cache:
        return 0
    cache.append((i, j))
    for d in range(4):
        v = i + vertical[d]
        h = j + horizontal[d]
        if not (0 <= v < len(area) and 0 <= h < len(area[0])):
            continue
        if area[v][j] < 9 and v != i:
            b += find_basin(area, v, j)
        if area[i][h] < 9 and h != j:
            b += find_basin(area, i, h)
    return b


def main():
    area = [[int(x) for x in line] for line in get_input()]

    basins = []
    for i in range(len(area)):
        for j in range(len(area[i])):
            if area[i][j] == 9:
                continue
            basins.append(find_basin(area, i, j))

    basins = sorted(basins, reverse=True)
    print(basins[0] * basins[1] * basins[2])


if __name__ == "__main__":
    main()
