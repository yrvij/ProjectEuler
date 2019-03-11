# Problem 28: Number spiral diagonals
import math

num = 1
sum = 1
x = 2
counter = 1

while int(math.sqrt(num)) != 1001:
    for i in range(4):
        num += x
        sum += num
    x += 2
    counter += 1
    
print(sum)
