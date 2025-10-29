# Input number of stones
N = int(input())

stones = N
i = 1  # round counter

while True:
    # Ramesh's turn
    if stones <= i:
        print("Ramesh")
        break
    stones -= i

    # Suresh's turn
    if stones <= i*2:
        print("Suresh")
        break
    stones -= i*2

    i += 1
