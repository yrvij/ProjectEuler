# Problem 48: Self powers -

i = 1
num = 0
while i <= 1000:
    num += i**i
    i += 1
    
num = str(num)
print(num[len(num)-10:])
    
