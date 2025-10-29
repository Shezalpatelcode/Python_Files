# Function to find last digit of a^b
def last_digit(a, b):
    if b == 0:
        return 1
    if a == 0:
        return 0
    
    # Last digit patterns repeat every 4 or fewer
    pattern = []
    last = a % 10
    pattern.append(last)
    
    # Build repeating cycle of last digits
    while True:
        last = (last * (a % 10)) % 10
        if last in pattern:
            break
        pattern.append(last)
    
    # Find which digit in cycle corresponds to b
    index = (b - 1) % len(pattern)
    return pattern[index]


# ---------- Main Program ----------
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(last_digit(a, b))
