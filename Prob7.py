# Problem 7: 10001st prime -

from sympy import sieve
target = 10001
primes = list(sieve.primerange(1,10**6))
print(primes[target-1])
