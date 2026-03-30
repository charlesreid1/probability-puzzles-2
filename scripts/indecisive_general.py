"""
The Indecisive General (The Leaf Node Puzzle)

A general organizes N battalions by randomly picking pivots and
recursively splitting (building a random BST). A "Frontline Unit"
is a battalion with no subordinates — a leaf node in the BST.

Expected number of leaf nodes in a random BST of N elements = (N+1)/3.

Drawn from TAOCP Volume 3: Sorting and Searching.
"""

# The Indecisive General
#
# Build a random BST by inserting 1..N in random order.
# Expected number of leaf nodes = (N+1)/3
#
# From: The Art of Computer Programming, Volume 3

import random


class BSTNode:
    __slots__ = ("val", "left", "right")

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert(root, val):
    if root is None:
        return BSTNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root


def count_leaves(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return count_leaves(root.left) + count_leaves(root.right)


def indecisive_general():
    samples = 200000

    for N in [10, 20, 50, 100, 500]:
        total_leaves = 0

        for _ in range(samples):
            order = list(range(1, N + 1))
            random.shuffle(order)
            root = None
            for val in order:
                root = insert(root, val)
            total_leaves += count_leaves(root)

        avg = total_leaves / samples
        expected = (N + 1) / 3

        print(f"N = {N}")
        print(f"  Simulated avg leaves: {avg:.2f}")
        print(f"  Expected (N+1)/3:     {expected:.2f}")
        print()


if __name__ == "__main__":
    indecisive_general()
