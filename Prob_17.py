# Problem 17: Number letter counts -

bases = {
        1 : "one",
        2 : "two",
        3 : "three",
        4 : "four",
        5 : "five",
        6 : "six",
        7 : "seven",
        8 : "eight",
        9 : "nine",
        10 : "ten",
        11 : "eleven",
        12 : "twelve",
        13 : "thirteen",
        14 : "fourteen",
        15 : "fifteen",
        16 : "sixteen",
        17 : "seventeen",
        18 : "eighteen",
        19 : "nineteen",
        20 : "twenty",
        30 : "thirty",
        40 : "forty",
        50 : "fifty",
        60 : "sixty",
        70 : "seventy",
        80 : "eighty",
        90 : "ninety"
    }
        
def generate_wordnumber(num):
    if num < 20:
        return bases[num]
    elif num >= 20 and num <= 99:
        if str(num)[1] == '0':
            return bases[num]
        else: 
            return bases[int(str(num)[0]) * 10] + ' ' + bases[int(str(num)[1])]
    elif len(str(num)) == 3:
        if str(num)[1] == str(num)[2] == '0':
            return bases[int(str(num)[0])] + ' hundred'
        elif str(num)[1] == '0':
            return bases[int(str(num)[0])] + ' hundred and ' + bases[int(str(num)[2])]
        elif str(num)[2] == '0':
            return bases[int(str(num)[0])] + ' hundred and ' + bases[int(str(num)[1]) * 10]
        elif str(num)[1] == '1':
            return bases[int(str(num)[0])] + ' hundred and ' + bases[int(str(num)[1:3])]
        else:
            return bases[int(str(num)[0])] + ' hundred and ' + bases[int(str(num)[1]) * 10] +  ' ' + bases[int(str(num)[2])]
    else:
        return "one thousand"
        
letters = 0
for i in range(1,1001):
    letters += len(generate_wordnumber(i).replace(' ',''))
    
print(letters)
