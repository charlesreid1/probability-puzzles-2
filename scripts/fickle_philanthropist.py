"""
The Fickle Philanthropist (The Reservoir Updates Puzzle)

A patron uses Algorithm R (reservoir sampling, K=1) on N paintings.
How many times does he swap the painting in his carriage?

Each painting i (for i >= 2) is kept with probability 1/i.
Expected swaps = sum_{i=2}^{N} 1/i = H_N - 1.

Drawn from TAOCP Volume 2: Seminumerical Algorithms.
"""

# The Fickle Philanthropist
#
# Reservoir sampling K=1: expected number of times the reservoir
# is overwritten = H_N - 1.
#
# From: The Art of Computer Programming, Volume 2

import random


def reservoir_sample_count_swaps(N):
    """Run Algorithm R on stream of N items, return number of swaps."""
    swaps = 0
    for k in range(2, N + 1):
        if random.random() < 1 / k:
            swaps += 1
    return swaps


def harmonic(n):
    return sum(1 / i for i in range(1, n + 1))


def fickle_philanthropist():
    samples = 500000

    for N in [10, 50, 100, 1000, 10000]:
        total_swaps = 0

        for _ in range(samples):
            total_swaps += reservoir_sample_count_swaps(N)

        avg = total_swaps / samples
        expected = harmonic(N) - 1

        print(f"N = {N}")
        print(f"  Simulated avg swaps: {avg:.4f}")
        print(f"  Expected (H_N - 1):  {expected:.4f}")
        print()


if __name__ == "__main__":
    fickle_philanthropist()
