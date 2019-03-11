# Problem 10: Summation of primes -

from sympy import sieve
primes = list(sieve.primerange(1,2000000))
print(sum(primes))
