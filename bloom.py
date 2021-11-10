from numpy.random import default_rng
from hashlib import md5

# To make results reproducible while making sure repeated generation of hash functions is random
SEED_GENERATOR = default_rng(42)
# I don't want to keep generating the same seeds over and over again
# It should be that k << BIG_RANGE
BIG_RANGE = 1000000


class BloomFilter:
    def __init__(self, n, k, hash_gen):
        self.array = [0] * n
        self.hashes = hash_gen(k, n)

    def add(self, i):
        for hash_f in self.hashes:
            self.array[hash_f(i)] = 1

    def query(self, i):
        for hash_f in self.hashes:
            if self.array[hash_f(i)] == 0:
                return False
            return True


def hash_1(k, n, seeds=None):
    # k := number of hash functions
    # n := size of table
    # seeds := optional seed values
    if not seeds:
        seeds = SEED_GENERATOR.integers(0, BIG_RANGE, k)
    elif len(seeds) != k:
        raise Exception(f"Number of seeds doesn't match k: {len(seeds)} != {k}")

    h = lambda i: lambda x: default_rng(seeds[i]+x).integers(0, n)
    hashes = [h(i) for i in range(k)]
    return hashes


def hash_2(k, n, a=None, b=None):  # unclear: needs n to be big prime?
    # k := number of hash functions
    # n := size of table
    # a := optional values for calculation
    # b := optional values for calculation
    if not a:
        a = SEED_GENERATOR.integers(1, n, k)
    elif len(a) != k:
        raise Exception(f"Number of a's doesn't match k: {len(a)} != {k}")
    if not b:
        b = SEED_GENERATOR.integers(0, n, k)
    elif len(b) != k:
        raise Exception(f"Number of b's doesn't match k: {len(b)} != {k}")

    h = lambda ai, bi: lambda x: (ai * x + bi) % n
    return [h(ai, bi) for ai, bi in zip(a, b)]


def bloom(N, n, m, a, t, b, k=3, hash_gen=hash_1):
    # N := size of domain (should be BIG)
    # n := size of bitarray
    # m := number of elements to be added
    # a := list of elements to be added (should be in range [0, N-1])
    # t := number of queries
    # b := list of elements to be queried (should be in range [0, N-1])
    # k := optional, number of hash functions the filter should use
    # hash := optional, hash function generator that should at least take k and n as input
    filter = BloomFilter(n, k, hash_gen)
    for item in a:
        filter.add(item)
    results = []
    for item in b:
        results.append(filter.query(item))
    return results
