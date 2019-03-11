# Problem 5: Smallest multiple -

def find_lcm(num1, num2): 
    if num1 > num2: 
        num = num1 
        den = num2 
    else: 
        num = num2 
        den = num1 
    rem = num % den 
    
    while rem != 0: 
        num = den 
        den = rem 
        rem = num % den 
        
    gcd = den 
    lcm = int(int(num1 * num2) / int(gcd)) 
    return lcm 
      
nums = list(range(1,21)) 
  
num1 = nums[0] 
num2 = nums[1] 
lcm = find_lcm(num1, num2) 
  
for i in range(2, len(nums)): 
    lcm = find_lcm(lcm, nums[i]) 
      
print(lcm) 
