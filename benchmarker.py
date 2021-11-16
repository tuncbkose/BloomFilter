import bloom
import numpy as np


def stats(list_of_counts):
	max_c = max(list_of_counts)
	min_c = min(list_of_counts)
	q25 = np.quantile(list_of_counts, .25)
	med = np.quantile(list_of_counts, .5)
	q75 = np.quantile(list_of_counts, .75)
	std = np.std(list_of_counts)
	return {"Max": max_c, "Min": min_c, "Q25": q25, "Med": med, "Q75": q75, "Std": std}


def part_1():
	# For every k and n in the for loops below, counts how many times each output in the codomain is encountered
	# This count happens for both hash functions generators
	# For each generator, we count both outputs across all k functions, and the outputs of only the first function
	# We also dump some basic statistics about each of these counts
	data = range(966966)

	for k in [1, 3, 5]:
		for n in [10, 30, 100]:
			print(f"Running n: {n}, k: {k}")

			# all hash functions vs only the first
			range_1_all = [0] * n
			range_2_all = [0] * n
			range_1_first = [0] * n
			range_2_first = [0] * n

			hashes_1 = bloom.hash_1(k, n)
			hashes_2 = bloom.hash_2(k, n)

			for i in data:
				range_1_first[hashes_1[0](i)] += 1
				range_2_first[hashes_2[0](i)] += 1
				hashes_p = zip(hashes_1, hashes_2)
				for hash_f1, hash_f2 in hashes_p:
					range_1_all[hash_f1(i)] += 1
					range_2_all[hash_f2(i)] += 1

			f_names = ["h1_all", "h2_all", "h1_first", "h2_first"]
			lists = [range_1_all, range_2_all, range_1_first, range_2_first]

			for f_name, l in zip(f_names, lists):
				with open(f"data/part1_n{n}_k{k}_{f_name}.txt", "w") as f:
					for i in l:
						f.write(f"{i}\n")
				with open(f"data/part1_n{n}_k{k}_{f_name}_stats.txt", "w") as f:
					for stat, v in stats(l).items():
						f.write(f"{stat}: {v}\n")


def part_2():
	N = 1  # doesn't seem to affect anything
	t = 100  # number of tests
	fp_results = []
	for k in [1, 3, 5]: # number of hash functions
		for n in [20, 40, 100]: # size of bitarray
			for m in [n//4, n//2, 3*n//4, n]: # number of elements added to filter
				# Every item being queried is not in filter
				results = bloom.bloom(N, n, m, range(m), t, range(m, m+t), k)
				fp = sum(results) / len(results)
				fp_results.append((k,n,m,fp))
	with open("data/part2.txt", "w") as f:
		f.write("k n t fp\n")
		for k, n, t, fp in fp_results:
			f.write(f"{k} {n} {t} {fp}\n")


if __name__ == "__main__":
	part_1()
	part_2()
