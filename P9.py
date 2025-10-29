# Read number of test cases
T = int(input())

for _ in range(T):
    N = int(input())
    # Package size that maximizes leftover
    A = N // 2 + 1
    print(A)
