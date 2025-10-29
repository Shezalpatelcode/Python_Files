# Read number of people
N = int(input())

# Read minimum skill required
X = int(input())

# Process each person's skill
for _ in range(N):
    Y = int(input())
    if Y >= X:
        print("YES")
    else:
        print("NO")
