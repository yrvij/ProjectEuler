# Problem 25: 1000-digit Fibonacci number -

first = 1
second = 1
counter = 2

while len(str(second)) < 1000:
    temp = second
    second += first
    first = temp
    counter += 1
    
print(counter)
