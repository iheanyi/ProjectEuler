import math


def square_sum(y):
	return int(math.pow(sum(range(1,y)), 2))

def sum_all_squares(num):
	return  sum(map(lambda x: int(math.pow(x,2)), range(1,num)))

def difference_squares(limit):
	return square_sum(limit)-sum_all_squares(limit)


square_numbers = map(lambda x: int(math.pow(x,2)), range(1,11))

print difference_squares(101)