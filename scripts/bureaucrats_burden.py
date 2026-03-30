"""
The Bureaucrat's Burden (The Total Path Length Puzzle)

N civil servants form a random BST. The "Burden" of each is the number
of bosses between them and the Supreme Minister (root). The total Burden
is the total internal path length of the random BST.

Expected total internal path length = 2N*H_N - 4N + 2*H_N
    = 2(N+1)*H_N - 4N
which for large N is approximately 2N*ln(N).

This equals the expected total comparisons in average-case Quicksort.

Drawn from TAOCP Volume 3: Sorting and Searching.
"""

# The Bureaucrat's Burden
#
# Total internal path length of a random BST of N nodes.
# Expected value = 2(N+1)*H_N - 4N
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


def total_path_length(root, depth=0):
    if root is None:
        return 0
    return depth + total_path_length(root.left, depth + 1) + total_path_length(root.right, depth + 1)


def harmonic(n):
    return sum(1 / i for i in range(1, n + 1))


def bureaucrats_burden():
    samples = 200000

    for N in [10, 20, 50, 100, 500]:
        total_pl = 0

        for _ in range(samples):
            order = list(range(1, N + 1))
            random.shuffle(order)
            root = None
            for val in order:
                root = insert(root, val)
            total_pl += total_path_length(root)

        avg = total_pl / samples
        expected = 2 * (N + 1) * harmonic(N) - 4 * N

        print(f"N = {N}")
        print(f"  Simulated avg total path length: {avg:.2f}")
        print(f"  Expected 2(N+1)*H_N - 4N:       {expected:.2f}")
        print()


if __name__ == "__main__":
    bureaucrats_burden()
