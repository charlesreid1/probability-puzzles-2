"""
The Infinite Hashway (The Collision Puzzle)

Miss Hashway is a librarian in a vast, circular library containing M empty
pedestals arranged in a giant ring. She places N magical books using linear
probing: roll an M-sided die, and if the pedestal is occupied, walk clockwise
until finding an empty spot.

The expected number of probes when inserting the N-th book into a table of
size M (with N-1 books already placed) is approximately:
    (1/2) * (1 + 1/(1 - alpha)^2)
where alpha = (N-1)/M is the load factor before insertion.

Drawn from TAOCP Volume 3: Sorting and Searching.
"""

# The Infinite Hashway
#
# Linear probing: insert N items into M slots.
# Expected probes for the N-th insertion ~ (1/2)(1 + 1/(1-alpha)^2)
# where alpha = (N-1)/M.
#
# From: The Art of Computer Programming, Volume 3

import random


def linear_probe_insert(table, M, val):
    """Insert val into table using linear probing. Return number of probes."""
    h = random.randrange(M)
    probes = 1
    while table[h] is not None:
        h = (h + 1) % M
        probes += 1
    table[h] = val
    return probes


def infinite_hashway():
    samples = 100000

    M = 1000
    target_N = 500  # placing the 500th book

    total_probes = 0
    for _ in range(samples):
        table = [None] * M
        for i in range(1, target_N + 1):
            p = linear_probe_insert(table, M, i)
            if i == target_N:
                total_probes += p

    avg_probes = total_probes / samples
    alpha = (target_N - 1) / M
    expected = 0.5 * (1 + 1 / (1 - alpha) ** 2)

    print(f"M = {M}, inserting book N = {target_N}")
    print(f"  Load factor alpha = (N-1)/M = {alpha:.3f}")
    print(f"  Simulated avg probes: {avg_probes:.2f}")
    print(f"  Expected (Knuth):     {expected:.2f}")
    print()

    # Show the trend across different load factors
    print("Probes vs load factor:")
    print(f"  {'N':>5}  {'alpha':>8}  {'Simulated':>10}  {'Expected':>10}")
    print(f"  {'':->5}  {'':->8}  {'':->10}  {'':->10}")

    for target in [100, 250, 500, 700, 900, 950]:
        total = 0
        for _ in range(samples):
            table = [None] * M
            for i in range(1, target + 1):
                p = linear_probe_insert(table, M, i)
                if i == target:
                    total += p
        avg = total / samples
        a = (target - 1) / M
        exp = 0.5 * (1 + 1 / (1 - a) ** 2)
        print(f"  {target:>5}  {a:>8.3f}  {avg:>10.2f}  {exp:>10.2f}")


if __name__ == "__main__":
    infinite_hashway()
