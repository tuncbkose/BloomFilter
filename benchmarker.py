import bloom

#this is my first time writing python code.



data = range(966966)


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


distribution = test_hash_2()

print(distribution)
print ("max of this distribution is ", max(distribution))
print ("min of this distribution is ", min(distribution))

