# Largest Palindrome Product
# Largest Palindrome of the product of two three-digit numbers
# Project Euler Problem 4
# Date: July 26, 2013

# Reverse the number by converting to string, backwards slicing
# then returning the string as an integer

factor_dict = dict()

def reverse_number(x):
	return int(str(x)[::-1])

# Function for asserting that number is a palindrome
def palindrome(x):
	return reverse_number(x) == x

# Check number of digits
def digits(number):
	return len(str(number))

# Assert that number has a length of three
def valid_multiply(number, x):
	if digits(number/x) == 3:
		return True
	else:
		return False

# Filter numbers with only 3 digit factors
def get_factors(number):
	# Map values to a dictionary
	global factor_dict
	values = filter(lambda x: number % x == 0 and valid_multiply(number, x), range(100, 999))
	if len(values) > 0:
		factor_dict[number] = values
	return values

# Lower limit will be 100*100, upper limit will 999*999
lower_limit = 100*100
upper_limit = 999*999

# Filter out all numbers between  the lower limit and the upper_limit that aren't palindromes
palindromes = filter(lambda x: palindrome(x), range(lower_limit, upper_limit))

# Then map these numbers to a dictionary
new_palindromes = map(lambda x: get_factors(x), palindromes)

# Then finding the largest is just a simple max call on the keys
largest = max(factor_dict.keys())


# Assertions here
print reduce(lambda x,y: x*y, factor_dict[largest])
assert reduce(lambda x,y: x*y, factor_dict[largest]) == largest, "INVALID MULTIPLIERS"
print "Largest palindrome from this set is: " + str(largest)
