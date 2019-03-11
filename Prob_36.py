# Problem 36: Double-base palindromes -

sum = 0
for i in range(1000001):
    if str(i) == str(i)[::-1] and str(bin(i)[2:]) == str(bin(i)[2:])[::-1]:
        sum += i
    
print(sum)
