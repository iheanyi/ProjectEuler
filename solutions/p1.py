#! /usr/local/bin/python

# Multiples of 3 and 5

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of
# these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.


# Rather than trying to implement a recursive solution, we can easily solve this in one line using
# lambda, filters, and the sum function
print sum(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(1000)))