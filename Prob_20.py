# Problem 20: Factorial digit sum -

i = 100
product = 1
while i != 0:
    product *= i
    i -= 1
sum = 0
for digit in str(product):
    sum += int(digit)
    
print(sum)
