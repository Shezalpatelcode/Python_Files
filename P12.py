import math

# Number of test cases
T = int(input())

for _ in range(T):
    X, Y = map(int, input().split())
    
    # Find GCD
    gcd = math.gcd(X, Y)
    
    # Find LCM using the formula
    lcm = (X * Y) // gcd
    
    # Print GCD and LCM
    print(gcd, lcm)
