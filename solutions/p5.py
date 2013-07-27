# Smallest Multiple
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def test_division(number, divisor):
	if number % divisor == 0:
		return True
	else:
		return False

start = 2500
while True:
	for number in range(1, 20):
		 result = test_division(start, number)
		 if result == False:
		 	print start
		 	start += 20
		 	break
	if result == True:
		break

print "End number is " + str(start)
