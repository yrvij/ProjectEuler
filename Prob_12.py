# Problem 12: Highly divisible triangular number -

import math
def num_divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            divisors.append(i)
            if i*i != n:
                divisors.append(int(n / i))
                
    return len(divisors)
                
i = 1
a = 1
while i < 100000000:
    if num_divisors(i) >= 500:
        print(str(i) + " : " + str(num_divisors(i)))
        break
    i += a + 1
    a += 1
