# Problem 14: Longest Collatz Sequence -

i = 1
steps = []

def collatz_steps(n):
    s = 0
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        s += 1
    return s

while i < 1000000:
    steps.append(collatz_steps(i))
    i += 1
    
print(steps.index(max(steps))+1)
