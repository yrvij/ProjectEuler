# Problem 39: Integer right triangles -

p = 1000

max_solutions = 0

for i in range(1,p+1):
    solutions = 0
    c, m = 0, 2
    while c < i:
        for n in range(1, m): 
            a = m * m - n * n 
            b = 2 * m * n 
            c = m * m + n * n 
            
            if c > i:
                break
            else:
                m += 1
    
