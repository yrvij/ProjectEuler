# Problem 23: Non-abundant sums -

import math
def divisors_sum(n):
    divisors = 0
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0 and n != 1:
            divisors += i
            if i * i != n:
                divisors += int(n / i)
    if (n != 1):
        divisors -= n
        
    return divisors

