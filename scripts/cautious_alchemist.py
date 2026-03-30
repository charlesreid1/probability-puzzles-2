"""
The Cautious Alchemist's Vial (The Stream Selection Puzzle)

An alchemist encounters a stream of vials from a magical spring. He can
only carry one vial home. He doesn't know how many vials the spring will
produce. What strategy ensures every vial has an equal chance of being chosen?

Strategy (Algorithm R, Reservoir Sampling for K=1):
When the k-th vial appears, keep it with probability 1/k.
This guarantees each of N vials is selected with probability 1/N.

Drawn from TAOCP Volume 2: Seminumerical Algorithms.
"""

# The Cautious Alchemist's Vial
#
# A stream of N items arrives one at a time. Maintain a single
# item such that after all N have been seen, each item had an
# equal 1/N probability of being the one kept.
#
# Algorithm R: keep the k-th item with probability 1/k.
#
# From: The Art of Computer Programming, Volume 2

import random


def reservoir_sample(stream):
    """Run Algorithm R on a stream, return the selected item."""
    chosen = None
    for k, item in enumerate(stream, start=1):
        if random.random() < 1 / k:
            chosen = item
    return chosen


def cautious_alchemist():
    samples = 500000

    for N in [5, 10, 20, 100]:
        counts = [0] * N
        stream = list(range(N))

        for _ in range(samples):
            chosen = reservoir_sample(stream)
            counts[chosen] += 1

        expected = 1 / N
        freqs = [c / samples for c in counts]
        max_dev = max(abs(f - expected) for f in freqs)

        print(f"N = {N}")
        print(f"  Expected frequency per item: {expected:.4f}")
        if N <= 10:
            for i, f in enumerate(freqs):
                print(f"  Item {i}: {f:.4f}")
        else:
            print(f"  Min frequency:  {min(freqs):.4f}")
            print(f"  Max frequency:  {max(freqs):.4f}")
        print(f"  Max deviation from uniform: {max_dev:.4f}")
        print()


if __name__ == "__main__":
    cautious_alchemist()
