"""
King Permutio's Dungeon (The Cycles Puzzle)

100 knights are imprisoned in 100 cells. The king shuffles 100 keys and
places one random key in each cell. The keys form chains: the key in
cell 1 might open cell 47, whose key opens cell 12, and so on.

What is the probability that the keys form one single cycle visiting
all 100 cells?

The probability that a random permutation of N elements is a single
cycle of length N is exactly 1/N.

Drawn from TAOCP Volume 1: Fundamental Algorithms.
"""

import random


def is_single_cycle(perm):
    """Check if permutation is a single cycle of length N."""
    N = len(perm)
    visited = 0
    pos = 0
    for _ in range(N):
        pos = perm[pos]
        visited += 1
        if pos == 0:
            break
    return visited == N


def king_permutios_dungeon():
    samples = 2000000

    for N in [10, 20, 50, 100]:
        single_cycle_count = 0

        for _ in range(samples):
            perm = list(range(N))
            random.shuffle(perm)
            if is_single_cycle(perm):
                single_cycle_count += 1

        p_sim = single_cycle_count / samples
        p_exact = 1 / N

        print(f"N = {N}")
        print(f"  P(single cycle) simulated: {p_sim:.6f}")
        print(f"  P(single cycle) exact 1/N: {p_exact:.6f}")
        print()


if __name__ == "__main__":
    king_permutios_dungeon()
