# Input three numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

# Using ternary operator to find maximum
max_num = a if (a > b and a > c) else (b if b > c else c)

# Display result
print("Maximum number is:", max_num)
