#!usr/bin/env python3.9

import itertools
import math
import sys
from collections import Counter, defaultdict, deque
from typing import Optional

sys.setrecursionlimit(9999999)

EXPLODE = 1
SPLIT = 2
BOTH = 3


def get_input():
    with open("input.txt", "r") as f:
        return [x.strip() for x in f.readlines()]


class Node:
    def __init__(self, value: int, parent=None) -> None:
        self.parent = parent
        self.value = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    def __str__(self) -> str:
        left = self.left and self.left.value
        right = self.right and self.right.value
        return f"Node(value={self.value}, depth={self.depth()}, children=({left}, {right}))"

    def listr(self):
        if self.value == -1:
            return f"[{self.left.listr()}, {self.right.listr()}]"
        else:
            return self.value

    def depth(self) -> int:
        if self.parent is None:
            return 0
        return self.parent.depth() + 1

    def split(self):
        v = self.value
        self.left = Node(math.floor(v / 2), self)
        self.right = Node(math.ceil(v / 2), self)
        self.value = -1

    def full_right(self):
        if self.right:
            return self.right.full_right()
        return self

    def full_left(self):
        if self.left:
            return self.left.full_left()
        return self

    def find_closest_node_on_left(self):
        curr = self
        while curr.parent.left == curr:
            curr = curr.parent
            if not curr.parent:
                return None
        return curr.parent.left.full_right()

    def find_closest_node_on_right(self):
        curr = self
        while curr.parent.right == curr:
            curr = curr.parent
            if not curr.parent:
                return None
        return curr.parent.right.full_left()

    def explode(self):
        print(f"exploding {str(self)})")
        next_left = self.find_closest_node_on_left()
        if next_left:
            print(f"next on left is {str(next_left)}")
            next_left.value += self.left.value

        next_right = self.find_closest_node_on_right()
        if next_right:
            print(f"next on right is {str(next_right)}")
            next_right.value += self.right.value

        self.value = 0
        self.right = None
        self.left = None

    def i_can_explode(self):
        if self.value != -1:
            return False
        if self.depth() >= 4 and self.right.value > -1 and self.left.value > -1:
            return True
        return False

    def i_can_split(self):
        return self.value > 9

    def someone_can_explode(self):
        if self.i_can_explode():
            return True
        if self.left and self.left.someone_can_explode():
            return True
        if self.right and self.right.someone_can_explode():
            return True

    def someone_can_split(self):
        if self.i_can_split():
            return True
        if self.left and self.left.someone_can_split():
            return True
        if self.right and self.right.someone_can_split():
            return True

    def traverse(self, action):
        if self.left is not None:
            if self.left.traverse(action):
                return 1

        if action == EXPLODE and self.i_can_explode():
            self.explode()
            return 1
        if action == SPLIT and self.i_can_split():
            self.split()
            return 1

        if self.right is not None:
            if self.right.traverse(action):
                return 1

    def print(self):
        print(self.listr())


def to_tree(chain, parent=None):
    if isinstance(chain, str):
        chain = eval(chain)
    if isinstance(chain, list):
        node = Node(-1, parent)
        node.left = to_tree(chain[0], node)
        node.right = to_tree(chain[1], node)
        return node
    elif isinstance(chain, (str, int)):
        return Node(int(chain), parent)


def magnitud(node):
    if node.value == -1:
        return 3 * magnitud(node.left) + 2 * magnitud(node.right)
    return node.value


def combine_trees(t1, t2):
    root = Node(-1)
    root.left = t1
    root.right = t2
    t1.parent = root
    t2.parent = root
    return root


def sum_trees(t1, t2):
    root = combine_trees(t1, t2)
    while root.someone_can_explode() or root.someone_can_split():
        while root.someone_can_explode():
            root.traverse(EXPLODE)
            root.print()
            print()
        if root.someone_can_split():
            root.traverse(SPLIT)
            root.print()
            print()
    return root


def main():
    # m1 = [[[[0, [4, 5]], [0, 0]], [[[4, 5], [2, 6]], [9, 5]]], [7, [[[3, 7], [4, 3]], [[6, 3], [8, 8]]]]]
    lines = get_input()
    result = to_tree(lines[0])
    for i in range(1, len(lines)):
        result = sum_trees(result, to_tree(lines[i]))
    result.print()
    print(magnitud(result))


if __name__ == "__main__":
    main()
