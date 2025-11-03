import math

#reversing the number to find if its really the palindrome or not
def rev(num):
    return int(num != 0) and ((num % 10) * \
            (10**int(math.log(num, 10))) + \
                        rev(num // 10))

#main part of the code 
num = 121
print ("The original number is : " + str(num))

res = num == rev(num)
print ("Is the number palindrome: " + str(res))