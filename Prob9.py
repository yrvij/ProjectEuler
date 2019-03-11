# Problem 9: Special Pythagorean triplet -

c, m = 0, 2
found = False

while c < 100: 
    for n in range(1, m): 
        a = m * m - n * n 
        b = 2 * m * n 
        c = m * m + n * n 
        
        print(a,b,c)

        if a + b + c == 1000:
            print(a*b*c) 
            found = True
            break
    if found:
        break
    else:
        m += 1
