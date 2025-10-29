# Input values
a = float(input("Enter the first term (a): "))
d = float(input("Enter the common difference (d): "))
n = int(input("Enter the number of terms (n): "))

# Calculate nth term
nth_term = a + (n - 1) * d

# Calculate sum of n terms
sum_n = (n / 2) * (2 * a + (n - 1) * d)

# Display results
print(f"\nThe {n}th term of the AP is: {nth_term}")
print(f"The sum of the first {n} terms is: {sum_n}")
