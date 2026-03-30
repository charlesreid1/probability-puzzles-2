"""
The Spies Who Watched Me (The Expected Cycles Puzzle)

N spies each watch exactly one other spy (random permutation).
The surveillance network forms closed loops (cycles).

Expected number of cycles in a random permutation of N = H_N.
P(Agent 007 is in a 2-cycle) = 1/N (since for a specific element,
the probability of being in a cycle of any given length k is 1/N).

Actually, P(specific element is in a cycle of length 2):
Agent i is in a 2-cycle iff sigma(sigma(i)) = i and sigma(i) != i.
P = (N-1) * (N-2)! / N! = 1/N ... wait, let me derive properly.
P(sigma(i) = j and sigma(j) = i) for some j != i = (N-1)/(N*(N-1)) = 1/N.

Drawn from TAOCP Volume 1: Fundamental Algorithms.
"""

# The Spies Who Watched Me
#
# Expected number of cycles in a random permutation of N = H_N.
# P(specific element is in a 2-cycle) = 1/N.
#
# From: The Art of Computer Programming, Volume 1

import random


def count_cycles(perm):
    """Count the number of cycles in a permutation."""
    N = len(perm)
    visited = [False] * N
    cycles = 0
    for i in range(N):
        if not visited[i]:
            cycles += 1
            j = i
            while not visited[j]:
                visited[j] = True
                j = perm[j]
    return cycles


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


def harmonic(n):
    return sum(1 / i for i in range(1, n + 1))


def spies_who_watched_me():
    samples = 500000

    for N in [10, 20, 50, 100]:
        total_cycles = 0
        agent_in_2cycle = 0

        for _ in range(samples):
            perm = list(range(N))
            random.shuffle(perm)
            total_cycles += count_cycles(perm)
            if cycle_length_of(perm, 0) == 2:
                agent_in_2cycle += 1

        avg_cycles = total_cycles / samples
        expected_cycles = harmonic(N)
        p_2cycle_sim = agent_in_2cycle / samples
        p_2cycle_exact = 1 / N

        print(f"N = {N}")
        print(f"  Avg cycles (simulated): {avg_cycles:.4f}")
        print(f"  Expected (H_N):         {expected_cycles:.4f}")
        print(f"  P(agent in 2-cycle) simulated: {p_2cycle_sim:.6f}")
        print(f"  P(agent in 2-cycle) exact 1/N: {p_2cycle_exact:.6f}")
        print()


if __name__ == "__main__":
    spies_who_watched_me()
