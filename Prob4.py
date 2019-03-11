# Problem 4: Largest palindrome product -

def check_pal(num):
    return str(num) == str(num)[::-1]
        
max_pal = 0
init = 100
i = 100
for j in range(100,1000):
    while i <= 999:
        product = init * i
        if check_pal(product) and max_pal < product:
            max_pal = product
        i += 1
    init += 1
    i = 100
    
print(max_pal)
