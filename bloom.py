from numpy.random import default_rng
import math

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


class CountingBloomFilter(BloomFilter):
    def __init__(self, n, k, hash_gen):
        super().__init__(n, k, hash_gen)
        self.counts = [0] * n

    def add(self, i):
        for hash_f in self.hashes:
            idx = hash_f(i)
            self.counts[idx] += 1
            self.array[idx] = 1

    def count(self, i):
        # returns (approximately) how many times i has been added
        c_min = math.inf
        for hash_f in self.hashes:
            idx = hash_f(i)
            c_min = min(c_min, self.counts[idx])
        return c_min

    def delete(self, i):
        # Trying to delete an item not in the filter can mess with counts of other items
        # There doesn't seem to be an easy fix for this, so the responsibility is left to the user
        for hash_f in self.hashes:
            idx = hash_f(i)
            self.counts[idx] -= 1
            if self.counts[idx] <= 0:
                self.array[idx] = 0


class DeletableBloomFilter(BloomFilter):
    def __init__(self, n, k, hash_gen, r):
        super().__init__(n, k, hash_gen)
        self.bitmap = [0] * r
        self.r = r

    def add(self, i):
        for hash_f in self.hashes:
            idx = hash_f(i)
            if self.array[idx] == 1:
                self.bitmap[idx % self.r] = 1
            else:
                self.array[idx] = 1

    def delete(self, i):
        # Deletion is not guaranteed but is likely
        deleted = False
        for hash_f in self.hashes:
            idx = hash_f(i)
            if self.bitmap[idx % self.r] == 0:
                self.array[idx] = 0
                deleted = True
        return deleted


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
