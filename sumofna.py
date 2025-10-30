def print_reverse(n):
    if n == 0:
        return
    print(n, end=' ')
    print_reverse(n - 1)

# Example
n = int(input("Enter a number: "))
print_reverse(n)
