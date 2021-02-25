def get_prime_factors(n):
	factors=list()
	divisor=2
	while (divisor <= n):
		if (n % divisor) == 0:
			factors.append(divisor)
			n = n/divisor
		else: 
			divisor +=1
	return factors

if __name__ == '__main__':
	print(get_prime_factors(630))
	print(get_prime_factors(13))

