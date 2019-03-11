# Problem 2: Even Fibonacci Numbers -

post = 1
prev = 1
sum = 0
while post < 4000000:
    temp = post
    post += prev
    prev = temp
    if post % 2 == 0:
        sum += post

print(sum)
