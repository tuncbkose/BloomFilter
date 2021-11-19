# BLOOM FILTER

## Detecting if something is in a set 

Bloom filters are a table of flags that we can use to determine if a given object is in a larger, harder-to-search set. It's time 
consuming to search a large database. Using a Bloom filter, we can drastically reduce the time it takes to see if something is in
a larger set. A given object will hash to `k` separate flags in the `n` length Bloom filter which we can quickly glance at to 
determine if the item is in a larger set. This filter doesn't have to be correct all the time, it's okay for the filter to 
accidentally have a hit when a hit isn't there. That's still a million times better than looking everything up all the time.

### removing things from a Bloom filter
You probably can't do this. This seems like a bad idea.

## Hash Functions
We had to design hash functions to do this. Both return lambdas that can be used to hash objects for a Bloom filter. Both also take 
`k` and `n` as inputs for the number of flags each object will trigger and the size of the Bloom filter respectively. 

### Hash 1
From what I gather, this is a normal hash function. Given an input, it will use a random number from our given seed to generate a 


### Hash 2


## TESTS AND BENCHMARKING
we tested the 2 hash functions to make sure they distributed everything evenly. We benchmarked hit rate also REEEEEE

### graphs are all even which is good
We want an even distribution because that means our hashes are distributing everything evenly. Below are some graphs that have been 
selected to show how even they are. I've hand checked all the graphs to make sure that they're all even. You can see all the graphs 
for yourself in the `data` directory. Once you see that, you'll see why we chose to omit most of them. it would have made this page 
incredibly long. You'll get the gist after a few of them. (I renege on all of this until the issue is fixed).

n = 10, k = 1, hash = 1 

all: <img src="data/part1_n10_k1_h1_all.png" alt="alt text" width="250px" height="250px">
first: <img src="data/part1_n10_k1_h1_first.png" alt="alt text" width="250px" height="250px">



n = 10, k = 1, hash = 2 

all: <img src="data/part1_n10_k1_h2_all.png" alt="alt text" width="250px" height="250px">
first: <img src="data/part1_n10_k1_h2_first.png" alt="alt text" width="250px" height="250px">



n = 10, k = 5, hash = 2 

all: <img src="data/part1_n10_k5_h2_all.png" alt="alt text" width="250px" height="250px">
first: <img src="data/part1_n10_k5_h2_first.png" alt="alt text" width="250px" height="250px">



n = 30, k = 5, hash = 2 

all: <img src="data/part1_n30_k5_h2_all.png" alt="alt text" width="250px" height="250px">
first: <img src="data/part1_n30_k5_h2_first.png" alt="alt text" width="250px" height="250px">



n = 100, k = 5, hash = 1 

all: <img src="data/part1_n100_k5_h1_all.png" alt="alt text" width="250px" height="250px">
first: <img src="data/part1_n100_k5_h1_first.png" alt="alt text" width="250px" height="250px">


n = 100, k = 3, hash = 2 

all: <img src="data/part1_n100_k3_h2_all.png" alt="alt text" width="250px" height="250px">
first: <img src="data/part1_n100_k3_h2_first.png" alt="alt text" width="250px" height="250px">



n = 100, k = 5, hash = 2 

all: <img src="data/part1_n100_k5_h2_all.png" alt="alt text" width="250px" height="250px">
first: <img src="data/part1_n100_k5_h2_first.png" alt="alt text" width="250px" height="250px">








### false positives
higher k is bad for false positives if theres a small n








