#!usr/bin/env python3.9
import itertools
from collections import defaultdict


def get_input():
    with open("input.txt", "r") as f:
        return [x.strip() for x in f.readlines()]


def big_cave(arg):
    return arg.isupper()


count = 0

G = defaultdict(list)
for con in get_input():
    a, b = con.split("-")
    G[a].append(b)
    G[b].append(a)


def dfs(node, path):
    path.append(node)
    if node == "end":
        global count
        count += 1
        return path
    for adj in G[node]:
        if adj in path and not big_cave(adj):
            continue
        dfs(adj, path.copy())


def main():
    dfs("start", [])
    print(count)


if __name__ == "__main__":
    main()
