# Largest Prime Factor
# Largest prime factor of the number 600851475143
import math



# List of Primes generated using the Sieve of Eratosthenes
def find_largest_prime_factor(n):
	# The threshold for largest factor will either be n or sqrt(n)

	limit = int(math.floor(math.sqrt(n)))

	# Generate numbers from 2 to the limit
	# in preparation for generating prime number sieve
	numbers = range(2,limit+1)
	if len(numbers) <= 1:
		return n

	# Filter out numbers from the list that aren't factors 
	# of n
	factors = filter(lambda x: n % x == 0, numbers)


	# Generate a sieve of prime factors from all factors
	i = 0
	start_index = factors[0]

	# Use Sieve of Eratoshenes method
	while i != len(factors):
		temp_list = factors
		for index, num in enumerate(factors):
			if num != start_index and num % start_index == 0:
				temp_list.remove(num)
		i += 1
		if i >= len(factors):
			break
		start_index =  factors[i]
		factors = temp_list

	largest_factor = max(factors)
	print "Largest prime factor for " + str(n) + " is " + str(largest_factor)
	return largest_factor

n = 600851475143
find_largest_prime_factor(n)