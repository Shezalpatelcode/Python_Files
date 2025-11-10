lst = [2, 3, 2, 4, 3, 5, 6]
seen = []
out = []

for x in lst:
    if x not in seen:
        seen.append(x)
        out.append(x)

print(out)  # [2, 3, 4, 5, 6]
