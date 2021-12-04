#!/usr/bin/env python3.9
def get_input() -> list[str]:
    with open("input.txt", "r") as f:
        return [x.strip() for x in f.readlines()]


class Box:
    def __init__(self) -> None:
        self.rows = []

    def row(self, i: int) -> list[str]:
        return self.rows[i]

    def add_row(self, line: str) -> None:
        self.rows.append([x.strip() for x in line.split(" ") if x.strip()])

    def nums_fill_any_row(self, nums: list[str]):
        for row in self.rows:
            nums_in_row = [x for x in row if x in nums]
            if len(nums_in_row) == len(row):
                return True

        return False

    def nums_fill_any_column(self, nums: list[str]):
        for i, _ in enumerate(self.rows):
            col = [x[i] for x in self.rows]
            nums_in_col = [x for x in col if x in nums]
            if len(nums_in_col) == len(col):
                return True

        return False

    def sum_unmarked(self, nums: list[str]):
        total = 0
        for row in self.rows:
            total += sum(int(x) for x in row if x not in nums)
        return total

    def __str__(self) -> str:
        return str(self.rows)

    def __repr__(self) -> str:
        return str(self.rows)


def get_boxes(puzzle):
    boxes: list[Box] = []

    current_box = Box()
    for i, line in enumerate(puzzle):
        if not line.strip():
            boxes.append(current_box)
            current_box = Box()
            continue

        current_box.add_row(line)
        if i == len(puzzle) - 1:
            boxes.append(current_box)

    return boxes


def solve():
    puzzle = get_input()

    entrance = puzzle[0].split(",")
    boxes = get_boxes(puzzle[2:])

    init = 5
    while 1:
        numbers = entrance[:init]
        last = entrance[init - 1]

        for box in boxes:
            if box.nums_fill_any_column(numbers) or box.nums_fill_any_row(numbers):
                print(box.sum_unmarked(numbers) * int(last))
                return

        init += 1


if __name__ == "__main__":
    solve()
