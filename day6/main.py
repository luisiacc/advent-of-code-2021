#!/usr/bin/env python3.9


def get_input() -> list[str]:
    with open("input.txt", "r") as f:
        return f.read()


DAYS = 80


def main():
    # 1 0 6 5 4 3 2 1 0 6 5 4 3 2 1 0 6 5 4 3 2 1
    #     8 7 6 5 4 3 2 1 0 6 5 4 3 2 1 0 6 5 4 3 2 1 0
    #                       8 7 6 5 4 3 2 1 0 6 5 4 3 2 1 0 6 5 4 3
    #     8 7 6 5 4 3 2 1 0 6 5 4 3 2 1 0
    lanterns = list(map(int, get_input().split(",")))
    for _ in range(DAYS):
        new_lanterns = []
        for i, lanter in enumerate(lanterns):
            lanterns[i] = lanter - 1
            if lanterns[i] == -1:
                lanterns[i] = 6
                new_lanterns.append(8)
        lanterns.extend(new_lanterns)

    print(len(lanterns))


if __name__ == "__main__":
    main()
