# Function to compute factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    fact = 1
    for i in range(2, n+1):
        fact *= i
    return fact

# Function to compute nCr (combinations)
def nCr(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

# Input number of rows
num_rows = int(input("Enter number of rows: "))

# Generate Pascal's Triangle
for r in range(num_rows):
    row = []
    for c in range(r + 1):
        row.append(str(nCr(r, c)))
    print(" ".join(row))
