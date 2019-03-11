# Problem 42: Coded triangle numbers -

def generateTriangularNumbers(num):
    tri_nums = []
    a = 0
    i = 1
    while a < num:
        n = int((1/2)*i*(i+1))
        tri_nums.append(n)
        a = n
        i += 1
        
    return tri_nums
    

words = []
with open("words.txt",'r') as file:
    for line in file:
        for word in line.split(','):
            words.append(word.strip("\""))
    file.close()
    
alpha_values = []
for item in words:
    tot = 0
    for char in item:
        tot += ord(char) - 64
    alpha_values.append(tot)
            
t_nums = generateTriangularNumbers(max(alpha_values))

counter = 0
for item in alpha_values:
    if item in t_nums:
        counter += 1
        

print(counter)
    

