"""
The Phantom's Promenade (The Unsuccessful Search Puzzle)

Miss Hashway has placed N books in M pedestals using linear probing.
A phantom searches for a book that isn't there: he starts at a random
pedestal and walks clockwise until finding an empty one.

Expected probes for an unsuccessful search in a linear probing table
with load factor alpha = N/M:
    (1/2) * (1 + 1/(1 - alpha)^2)

Drawn from TAOCP Volume 3: Sorting and Searching.
"""

# The Phantom's Promenade
#
# Unsuccessful search in a linear probing hash table.
# Expected probes ~ (1/2)(1 + 1/(1-alpha)^2) where alpha = N/M.
#
# From: The Art of Computer Programming, Volume 3

import random


def build_table(M, N):
    """Insert N items into a table of size M using linear probing."""
    table = [False] * M
    for _ in range(N):
        h = random.randrange(M)
        while table[h]:
            h = (h + 1) % M
        table[h] = True
    return table


def unsuccessful_search_probes(table, M):
    """Probe from a random position until hitting an empty slot."""
    h = random.randrange(M)
    probes = 1
    while table[h]:
        h = (h + 1) % M
        probes += 1
    return probes


def phantoms_promenade():
    samples = 200000
    M = 1000

    print(f"M = {M}")
    print(f"  {'N':>5}  {'alpha':>8}  {'Simulated':>10}  {'Expected':>10}")
    print(f"  {'':->5}  {'':->8}  {'':->10}  {'':->10}")

    for N in [100, 250, 500, 700, 800, 900]:
        total_probes = 0

        for _ in range(samples):
            table = build_table(M, N)
            total_probes += unsuccessful_search_probes(table, M)

        avg = total_probes / samples
        alpha = N / M
        expected = 0.5 * (1 + 1 / (1 - alpha) ** 2)

        print(f"  {N:>5}  {alpha:>8.3f}  {avg:>10.2f}  {expected:>10.2f}")

    print()


if __name__ == "__main__":
    phantoms_promenade()
