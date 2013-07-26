# Even Fibonacci
# By considering the terms in the Fibonacci sequence whose 
# values do not exceed four million, find the sum of the even-valued terms.

def even_fibo():
	a = 1
	b = 2
	fibo_sum = b
	while True:
		a,b = b, a+b
		if b > 4000000:
			break
		if b % 2 == 0:
			fibo_sum += b
	return fibo_sum

print even_fibo()