"""
The Dispatcher's Dilemma (The Runs Puzzle)

A courier delivers N edicts to manors along a one-way road. He reads
edicts from a shuffled pile. If the next manor is further East, he
continues. If it's behind him, he must return to the castle and start
a new journey.

The expected number of ascending runs in a random permutation of N
is (N+1)/2.

Drawn from TAOCP Volume 3: Sorting and Searching.
"""

# The Dispatcher's Dilemma
#
# Expected number of ascending runs in a random permutation
# of N elements = (N+1)/2.
#
# From: The Art of Computer Programming, Volume 3

import random


def count_ascending_runs(perm):
    """Count the number of ascending runs in a permutation."""
    if not perm:
        return 0
    runs = 1
    for i in range(1, len(perm)):
        if perm[i] < perm[i - 1]:
            runs += 1
    return runs


def dispatchers_dilemma():
    samples = 500000

    for N in [5, 10, 20, 50, 100]:
        total_runs = 0

        for _ in range(samples):
            perm = list(range(N))
            random.shuffle(perm)
            total_runs += count_ascending_runs(perm)

        avg = total_runs / samples
        expected = (N + 1) / 2

        print(f"N = {N}")
        print(f"  Simulated avg runs: {avg:.4f}")
        print(f"  Expected (N+1)/2:   {expected:.4f}")
        print()


if __name__ == "__main__":
    dispatchers_dilemma()
