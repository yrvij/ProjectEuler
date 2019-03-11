# Problem 21: Amicable numbers -

import math
def d(n):
    divisors = 0
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0 and n != 1:
            divisors += i
            if i * i != n:
                divisors += int(n / i)
    if (n != 1):
        divisors -= n
        
    return divisors

sum = 0
amicable = []
for i in range(1,10001):
    if d(d(i)) == i and d(i) != i and d(i) != 1 and d(i) != 0 and d(i) not in amicable:
        sum += i + d(i)
        amicable.append(i)
        amicable.append(d(i))
    
print(amicable)
print(sum)
