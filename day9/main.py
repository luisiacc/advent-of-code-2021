#!usr/bin/env python3.9
def get_input():
    with open("input.txt", "r") as f:
        return [x.strip() for x in f.readlines()]


def main():
    area = [[int(x) for x in line] for line in get_input()]

    c = 0
    vertical = (1, 0, -1, 0)
    horizontal = (0, 1, 0, -1)
    for row, line in enumerate(area):
        for col, num in enumerate(line):
            low = True
            for d in range(4):
                v = row + vertical[d]
                h = col + horizontal[d]
                if (
                    0 <= v < len(area)
                    and 0 <= h < len(line)
                    and (num > area[v][col] or num > area[row][h])
                ):
                    low = False
            if low and num != 9:
                print(row, col, num)
                c += num + 1

    print(c)


if __name__ == "__main__":
    main()
