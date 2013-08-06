# CJAA 6/9/2013
# Project Euler Problem 14
# Find the seed number under 1,000,000 that produces the longest Collatz sequence

def collatz(x):
	if x%2 == 0:
		return x/2
	else:
		return 3*x + 1

j = 2
longest_seed = 0
longest_chain = 0
longest_chain_path = []
chain = []
result = 0

while j < 1000000:
	chain.append(j)
	result = collatz(j)
	chain.append(result)

	while result != 1:
		result = collatz(result)
		chain.append(result)
	
	#print(j, len(chain), chain)
 
	if len(chain) > longest_chain:
		longest_seed = j
		longest_chain = len(chain)
		longest_chain_path = chain
		
	j += 1
	result = 0
	chain = []

print(longest_seed, longest_chain, longest_chain_path)