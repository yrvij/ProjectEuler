# Problem 3: Largest prime factor -

import math 
factors = []
num = 600851475143
while num % 2 == 0:
    factors.append(2)
    num /= 2

for i in range(3, int(math.sqrt(num)) + 1,2):
    while (num % i == 0):
        factors.append(i)
        num /= i

if (num > 2):
    factors.append(num)
        
print(max(factors));
