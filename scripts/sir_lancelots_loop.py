"""
Sir Lancelot's Loop (The Specific Cycle Puzzle)

100 prisoners, 100 cells, 100 randomly shuffled keys. Sir Lancelot
is in Cell 1. What is the probability his cycle has exactly length K?

For a specific element in a random permutation of N, the probability
of being in a cycle of length K is exactly 1/N for every K from 1 to N.

Every possible cycle length is equally likely — a result of staggering
simplicity.

Drawn from TAOCP Volume 1: Fundamental Algorithms.
"""

import random


def cycle_length_of(perm, start):
    """Return the length of the cycle containing 'start'."""
    length = 0
    j = start
    while True:
        j = perm[j]
        length += 1
        if j == start:
            break
    return length


def sir_lancelots_loop():
    samples = 2000000
    N = 100

    cycle_counts = [0] * (N + 1)  # index 1..N

    for _ in range(samples):
        perm = list(range(N))
        random.shuffle(perm)
        k = cycle_length_of(perm, 0)
        cycle_counts[k] += 1

    expected = 1 / N
    print(f"N = {N}, Sir Lancelot is element 0")
    print(f"Expected P(cycle length = K) = 1/N = {expected:.6f} for all K")
    print()

    # Show a selection of cycle lengths
    print(f"  {'K':>5}  {'Simulated':>10}  {'Exact':>10}")
    print(f"  {'':->5}  {'':->10}  {'':->10}")
    for k in [1, 2, 3, 5, 10, 25, 47, 50, 75, 99, 100]:
        p_sim = cycle_counts[k] / samples
        print(f"  {k:>5}  {p_sim:>10.6f}  {expected:>10.6f}")

    print()
    # Verify uniformity: max deviation
    freqs = [cycle_counts[k] / samples for k in range(1, N + 1)]
    max_dev = max(abs(f - expected) for f in freqs)
    print(f"  Max deviation from 1/N across all K: {max_dev:.6f}")


if __name__ == "__main__":
    sir_lancelots_loop()
