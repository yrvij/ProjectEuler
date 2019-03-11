# Problem 40: Champernowne's constant -

champ_const = "."
product = 1
for i in range(1,1000001):
    champ_const += str(i)

for i in range(7):
    product *= int(champ_const[10**i])
    
print(product)
