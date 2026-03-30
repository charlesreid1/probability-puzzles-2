"""
The Archivist's Epiphany (The Left-to-Right Maxima Puzzle)

An archivist reads N shuffled decrees. He transcribes a decree only if it
is strictly older than every decree he has read so far (a left-to-right
maximum).

Expected number of transcriptions = H_N (the N-th Harmonic number).
P(exactly k transcriptions in N decrees) = |s(N,k)| / N!
where |s(N,k)| is the unsigned Stirling number of the first kind.

For N=100, P(exactly 2) = |s(100,2)| / 100!

Drawn from TAOCP Volume 1 & 3.
"""

import random


def count_left_to_right_maxima(perm):
    """Count elements that are larger than all preceding elements."""
    count = 0
    current_max = -1
    for x in perm:
        if x > current_max:
            count += 1
            current_max = x
    return count


def harmonic(n):
    return sum(1 / i for i in range(1, n + 1))


def archivists_epiphany():
    samples = 500000

    for N in [10, 20, 50, 100]:
        total_maxima = 0
        exactly_two = 0

        for _ in range(samples):
            perm = list(range(N))
            random.shuffle(perm)
            m = count_left_to_right_maxima(perm)
            total_maxima += m
            if m == 2:
                exactly_two += 1

        avg = total_maxima / samples
        expected = harmonic(N)
        p_two_sim = exactly_two / samples

        print(f"N = {N}")
        print(f"  Expected maxima (H_N):  {expected:.4f}")
        print(f"  Simulated avg maxima:   {avg:.4f}")

        # For P(exactly 2), the exact value is |s(N,2)|/N! = H_{N-1}/N
        # since |s(N,2)| = (N-1)! * H_{N-1}
        p_two_exact = harmonic(N - 1) / N
        print(f"  P(exactly 2) simulated: {p_two_sim:.6f}")
        print(f"  P(exactly 2) exact:     {p_two_exact:.6f}")
        print()


if __name__ == "__main__":
    archivists_epiphany()
