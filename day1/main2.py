#!/usr/bin/env python3.9
def get_input():
    with open("sample.txt", "r") as f:
        return [x.strip() for x in f.readlines()]


def main():
    records = list(map(int, get_input()))
    count = 0
    i = 1
    while i + 2 < len(records):
        sum1 = records[i-1] + records[i] + records[i+1]
        sum2 = records[i] + records[i+1] + records[i+2]
        count += int(sum2 > sum1)
        i += 1

    print(count)


if __name__ == "__main__":
    main()
