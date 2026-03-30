"""
The Fractious Tour Guide (The Tree Depth Puzzle)

A tour guide recursively splits N tourists by randomly choosing pivots
(building a random BST). How many times is the k-th shortest tourist
moved before becoming a pivot themselves?

This equals the depth of element k in a random BST, which is also the
number of comparisons to find element k during Quicksort.

Expected depth of element k = H_k + H_{N+1-k} - 2
where H_n is the n-th harmonic number.

Drawn from TAOCP Volume 3: Sorting and Searching.
"""

# The Fractious Tour Guide
#
# Build a random BST by inserting 1..N in random order.
# The depth of element k equals the number of times that
# tourist is split into a subgroup before being chosen as pivot.
#
# Expected depth of k = H_k + H_{N+1-k} - 2
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


def find_depth(root, val):
    depth = 0
    node = root
    while node is not None:
        if val == node.val:
            return depth
        elif val < node.val:
            node = node.left
        else:
            node = node.right
        depth += 1
    return -1


def harmonic(n):
    return sum(1 / i for i in range(1, n + 1))


def expected_depth(k, N):
    return harmonic(k) + harmonic(N + 1 - k) - 2


def fractious_tour_guide():
    samples = 100000

    for N in [10, 50, 100, 500]:
        # Choose several k values: first, quarter, median, three-quarter, last
        ks = sorted(set([1, max(1, N // 4), max(1, N // 2), max(1, 3 * N // 4), N]))

        # Build many random BSTs, measure depth of each k
        totals = {k: 0 for k in ks}

        for _ in range(samples):
            order = list(range(1, N + 1))
            random.shuffle(order)
            root = None
            for val in order:
                root = insert(root, val)
            for k in ks:
                totals[k] += find_depth(root, k)

        print(f"N = {N}")
        print(f"  {'k':>6}  {'Simulated':>10}  {'Expected':>10}  {'Formula'}")
        print(f"  {'':->6}  {'':->10}  {'':->10}  {'':->30}")
        for k in ks:
            avg = totals[k] / samples
            exp = expected_depth(k, N)
            print(f"  {k:>6}  {avg:>10.2f}  {exp:>10.2f}  H_{k} + H_{N+1-k} - 2")
        print()


if __name__ == "__main__":
    fractious_tour_guide()
