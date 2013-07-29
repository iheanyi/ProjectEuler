# 10001st prime
# Find the 10001st prime number
# 
import math
def generate_primes(n):
	p = 2
	primes = [p]
	p += 1
	primes.append(p)

	while len(primes) != n:

		p += 2

		test_prime = True


		# Limit should only be up to the square root of current p, because nothing will exceed that.
		sqrt_limit = math.sqrt(p)
		for num in primes:
			if num > sqrt_limit:
				break
			if p % num == 0:
				test_prime = False
				break
		if test_prime:
			primes.append(p)

	return primes

primes = generate_primes(10001)
print primes[-1]
#print primes[10001]