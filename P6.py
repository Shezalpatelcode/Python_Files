# Function to reverse a number (integer)
def reverse_num(n):
    return int(str(n)[::-1])

# Read number of test cases
N = int(input())

# Process each test case
for _ in range(N):
    a, b = input().split()
    # Reverse both numbers
    rev_a = reverse_num(a)
    rev_b = reverse_num(b)
    
    # Add them and reverse the sum
    rev_sum = reverse_num(rev_a + rev_b)
    
    # Print the result (no leading zeros automatically)
    print(rev_sum)
