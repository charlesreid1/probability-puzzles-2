"""
The King's Council (The K-Reservoir Puzzle)

A King forms a Council of K=5 advisors from an endless stream of wise
people. When meeting the N-th person (N > K), he invites them with
probability K/N, and if invited, dismisses a random current advisor.

This is Algorithm R (Reservoir Sampling) generalized to K items.
Each of the N people seen so far has exactly K/N probability of being
on the council.

The expected number of replacements after the initial K are filled is:
    K * (H_N - H_K)
where H_n is the n-th harmonic number.

Drawn from TAOCP Volume 2: Seminumerical Algorithms.
"""

# The King's Council
#
# Reservoir sampling with K=5: maintain a uniform random sample
# of K items from a stream of N.
# P(select N-th item) = K/N
# Expected replacements = K * (H_N - H_K)
#
# From: The Art of Computer Programming, Volume 2

import random


def reservoir_sample_k(stream, K):
    """Run Algorithm R with reservoir size K. Return (reservoir, replacement_count)."""
    reservoir = list(stream[:K])
    replacements = 0
    for i in range(K, len(stream)):
        j = random.randint(0, i)  # 0 to i inclusive
        if j < K:
            reservoir[j] = stream[i]
            replacements += 1
    return reservoir, replacements


def harmonic(n):
    return sum(1 / i for i in range(1, n + 1))


def kings_council():
    samples = 500000
    K = 5

    for N in [20, 50, 100, 1000]:
        counts = [0] * N
        total_replacements = 0
        stream = list(range(N))

        for _ in range(samples):
            reservoir, reps = reservoir_sample_k(stream, K)
            total_replacements += reps
            for item in reservoir:
                counts[item] += 1

        expected_freq = K / N
        freqs = [c / samples for c in counts]
        max_dev = max(abs(f - expected_freq) for f in freqs)

        avg_reps = total_replacements / samples
        expected_reps = K * (harmonic(N) - harmonic(K))

        print(f"N = {N}, K = {K}")
        print(f"  Expected frequency per item (K/N): {expected_freq:.4f}")
        print(f"  Max deviation from uniform:        {max_dev:.4f}")
        print(f"  Avg replacements:   {avg_reps:.2f}")
        print(f"  Expected K*(H_N-H_K): {expected_reps:.2f}")
        print()


if __name__ == "__main__":
    kings_council()
