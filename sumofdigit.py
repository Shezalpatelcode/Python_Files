#sum_digits=lambda n: sum(int (digit) for digit in str(n))
#num=12345
#print("Sum of digits", sum_digits(num))

#new way ---
from functools import reduce
num=12345
digits=list(map(int,str(num))) #['1','2','3','4','5']

sum_of_digits=reduce(lambda x,y:x+y,digits)
print("SUM OF dIGITS",sum_of_digits)