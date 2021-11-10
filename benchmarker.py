import bloom

#this is my first time writing python code.




def test_hash_1():
	list_of_hashes = bloom.hash_1(3, 256)

	this_better_be_uniform = [0] * 256

	for item in data:
		for hash_ in list_of_hashes:
			hash_val = hash_(item)
			this_better_be_uniform[hash_val] += 1

	print(this_better_be_uniform)


def test_hash_2():
	list_of_hashes = bloom.hash_2(3, 256)

	this_better_be_uniform = [0] * 256

	for item in data:
		for hash_ in list_of_hashes:
			hash_val = hash_(item)
			this_better_be_uniform[hash_val] += 1

	return this_better_be_uniform




#I AM A PYTHON GOD
def part_1():
	data = range(966966)
	
	distribution = test_hash_2()
	#distribution = test_hash_1()

	print(distribution)
	print ("max of this distribution is ", max(distribution))
	print ("min of this distribution is ", min(distribution))



def test_bloom_with_hash_1():

	list_of_false_positives = bloom.bloom(1000966, 256, 128, range(128), 128, range(128,256), 1)
	false_positive_rate = sum(list_of_false_positives) / len(list_of_false_positives)
	print(false_positive_rate)


def test_bloom_with_hash_2():

	bloom.bloom(N, n, m, a, t, b, k, bloom.hash_2)


for i in range(10):
	test_bloom_with_hash_1()
