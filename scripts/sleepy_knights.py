"""
The Sleepy Knights of the Round Table (The Clustering Puzzle)

M knights, M chairs arranged in a circle. Each knight has a random
favorite chair. If occupied, they walk clockwise until finding an empty
one. Since M = M, the table fills completely.

What is the probability that the very last knight gets his favorite chair?

This is the Parking Problem. The probability that all M knights can park
(i.e., the table fills) using the circular variant is (M+1)^(M-1) / M^M
(Pollak's formula). But here M chairs = M knights, so the table always fills.

For the last knight to get his favorite chair, his favorite must still be
empty after M-1 knights have been seated. The probability the last knight
gets his favorite is 1/M (by symmetry of the parking function).

Drawn from TAOCP Volume 3: Sorting and Searching.
"""

import random


def seat_knights(M):
    """Seat M knights at M chairs. Return whether last knight got their favorite."""
    chairs = [False] * M
    favorites = [random.randrange(M) for _ in range(M)]

    for i in range(M):
        pos = favorites[i]
        while chairs[pos]:
            pos = (pos + 1) % M
        chairs[pos] = True
        if i == M - 1:
            return pos == favorites[i]

    return False


def sleepy_knights():
    samples = 1000000

    for M in [10, 20, 50, 100]:
        last_got_fav = 0

        for _ in range(samples):
            if seat_knights(M):
                last_got_fav += 1

        p_sim = last_got_fav / samples
        p_exact = 1 / M

        print(f"M = {M}")
        print(f"  P(last gets favorite) simulated: {p_sim:.6f}")
        print(f"  P(last gets favorite) exact 1/M: {p_exact:.6f}")
        print()


if __name__ == "__main__":
    sleepy_knights()
