"""
The Careless Typesetter's Toll (The Inversion Puzzle)

A careless typesetter drops a perfectly ordered manuscript of N pages,
resulting in a random permutation. He sorts it by swapping adjacent
out-of-order pages. How many swaps does he expect to make?

The expected number of inversions in a random permutation of N is N(N-1)/4.
The probability of exactly zero swaps is 1/N! (only the sorted permutation).
The probability of exactly one swap is (N-1)/N! (swap any one adjacent pair).

Drawn from TAOCP Volume 3: Sorting and Searching.
"""

# The Careless Typesetter's Toll
#
# A careless typesetter drops a manuscript of N numbered pages,
# producing a random permutation. He restores order by repeatedly
# swapping adjacent out-of-order pages (bubble sort).
#
# Expected swaps = N(N-1)/4
# P(zero swaps)  = 1/N!
# P(one swap)    = (N-1)/N!
#
# From: The Art of Computer Programming, Volume 3

import random
from math import factorial


def count_inversions(perm):
    """Count the number of inversions in a permutation."""
    n = len(perm)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if perm[i] > perm[j]:
                count += 1
    return count


def careless_typesetter():
    samples = 200000

    for N in [5, 10, 20, 52]:
        total_inversions = 0
        zero_count = 0
        one_count = 0

        for _ in range(samples):
            perm = list(range(N))
            random.shuffle(perm)
            inv = count_inversions(perm)
            total_inversions += inv
            if inv == 0:
                zero_count += 1
            elif inv == 1:
                one_count += 1

        avg = total_inversions / samples
        expected = N * (N - 1) / 4

        print(f"N = {N}")
        print(f"  Average inversions:  {avg:.2f}")
        print(f"  Expected (N(N-1)/4): {expected:.2f}")

        if N <= 10:
            p_zero_sim = zero_count / samples
            p_zero_exact = 1 / factorial(N)
            p_one_sim = one_count / samples
            p_one_exact = (N - 1) / factorial(N)
            print(f"  P(zero swaps): {p_zero_sim:.6f}  (exact: {p_zero_exact:.6f})")
            print(f"  P(one swap):   {p_one_sim:.6f}  (exact: {p_one_exact:.6f})")

        print()


if __name__ == "__main__":
    careless_typesetter()
