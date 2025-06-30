def gcd(a: int, b: int) -> int:
	"""Calculates the GCD between 2 numbers a and b

	Args:
		a (int)
		b (int)

	Returns:
		int: The GCD of a and b
	"""
	q = a//b
	r = a%b

	while r > 0:
		a = b
		b = r
		q = a//b
		r = a%b

	return b

# code from https://brilliant.org/wiki/extended-euclidean-algorithm/#extended-euclidean-algorithm
def extended_gcd(a: int, b: int) -> tuple[int,int,int]:
	"""The extended GCD algorithm that returns GCD and the coefficients
	for the linear combination of a nd b to get the GCD

	Args:
		a (int)
		b (int)

	Returns:
		tuple[int,int,int]: (GCD, x, y) in the equation x\*a + y\*b = gcd(a,b)
	"""
    # finding u,v, gcd(a,b) such that
	# x*a + y*b = gcd(a,b)
	x,y, u,v = 0,1, 1,0
	while a != 0:
		q, r = b//a, b%a
		m, n = x-u*q, y-v*q
		b,a, x,y, u,v = a,r, u,v, m,n
	gcd = b
	return gcd, x, y

# test for quadratic residue using Euler Condition
def legendre_symbol(x: int, p: int) -> int:
	"""Returns the Legendre Symbol of a number x in the Zp

	Args:
		x (int): number less than p
		p (int): prime number

	Returns:
		int: The Legendre Symbol of x in Zp
	"""
	exponent = (p-1)//2
	return pow(x, exponent, p)

def possible_quadratic_residues(candidates: list[int], p: int) -> list[int]:
	"""Given a list of integers and a prime p, returns a list of possible quadratic residues

	Args:
		candidates (list[int]): Integers to test for the property
		p (int): A prime number

	Returns:
		list[int]: List of possible quadratic residues in Zp
	"""
	residues = []
	for x in candidates:
		if legendre_symbol(x, p) == 1:
			residues.append(x)

	return residues

def three_mod_four_roots(a: int, p: int) -> tuple[int, int]:
	"""The roots of a quadratic residue assuming the prime p = 3 mod 4

	Args:
		a (int): a quadratic residue in Zp
		p (int): A prime number

	Returns:
		tuple[int, int]: Roots of a in Zp
	"""
	root = pow(a, (p+1)//4, p)

	return (root, p - root)

# implementation of the Tonelli-Shanks Algorithm
# reference here: https://en.wikipedia.org/wiki/Tonelli%E2%80%93Shanks_algorithm#The_algorithm
def tonelli_shanks(n: int, p: int) -> tuple[int, int]:
	"""The roots of a quadratic residue assuming the prime p = 1 mod 4

	Args:
		a (int): a quadratic residue in Zp
		p (int): A prime number

	Returns:
		tuple[int, int]: Roots of a in Zp
	"""
	assert legendre_symbol(n,p) == 1

	q = p - 1
	s = 0
	while q%2 == 0:
		q //= 2
		s += 1

	assert p-1 == q * pow(2, s)

	z = 0
	for x in range(2, p):
		if legendre_symbol(x, p) != 1:
			z = x
			break

	m = s
	c = pow(z, q, p)
	t = pow(n, q, p)
	r = pow(n, (q+1)//2, p)

	while True:
		if t == 0:
			r = 0
			break

		if t == 1:
			break

		if m == 1:
			print("No solution")
			return(0,0)

		for i in range(1, m):
			exponent = pow(2, i)
			if pow(t, exponent, p) == 1:
				power_of_2 = pow(2, m-i-1)
				b = pow(c, power_of_2, p)
				m = i
				c = pow(b, 2, p)
				t = (t * pow(b, 2, p)) % p
				r = (r * b) % p
				break

			if i == m-1:
				print("No solution")
				return(0,0)

	return (r, p-r)

# adapted from explanation here: https://en.wikipedia.org/wiki/Chinese_remainder_theorem#Using_the_existence_construction
def chinese_remainder_theorem(congruences):
	"""Given a list of congruences of (a_i, n_i),
	gives the result of the chinese remainder theorem to find a unique integer that fits the congruences

	Args:
		congruences (list[tuple(int, int]]): list of congruences of (a_i, n_i) where all n_i, n_j has gcd(n_i, n_j) = 1 when i !=j

	Returns:
		int: the integer that when mod all n in the congruences gives the corresponding a
	"""
	a_1, n_1 = congruences[0]

	for i in range(1, len(congruences)):
		a_2, n_2 = congruences[i]

		gcd, u, v = extended_gcd(n_1, n_2)

		# must be true for Chinese Remainder Theorem to work
		assert gcd == 1

		a_1 = a_2*n_1*u + a_1*n_2*v
		n_1 = n_1*n_2

		if abs(a_1) > a_1%n_1:
			a_1 = a_1 % n_1

	return a_1 % n_1

def euler_totient(prime_factors: list[tuple[int, int]]) -> int:
	"""Given the prime factorization of a number, calculates the Euler Totient or Euler Phi function

	Args:
		prime_factors (list[tuple[int, int]]): prime factors in the form (prime, power)

	Returns:
		int: The Euler Totient of the factorization
	"""
	totient = 1

	for factor in prime_factors:
		prime = factor[0]
		power = factor[1]

		totient *= (pow(prime, power) - pow(prime, power-1))

	return totient
