# Problem 22: Names scores -

names = []
with open("names.txt",'r') as file:
    for line in file:
        for name in line.split(','):
            names.append(name.strip("\""))
      
    file.close()

tot_name_score = 0
names = sorted(names)
for i,name in enumerate(names):
    alpha_pos = i + 1
    alpha_val = 0
    for char in name:
        alpha_val += ord(char) - 64
    tot_name_score += alpha_val * alpha_pos
print(tot_name_score)
    
