def recurSum(n):

    if n==0:
        return 0
    return n + recurSum(n-1)


num=3
result=recurSum(num)
print(f"The sum of the first {num} natural numbers is: {result}")
