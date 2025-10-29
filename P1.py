import math

# Given values
angle = 60  # degrees
radius = 42

# Step 1: find arc length
arc_length = (angle / 360) * 2 * math.pi * radius

# Step 2: find side of square
side = arc_length / 4

# Step 3: find area of square
area = side ** 2

print(f"Arc Length: {arc_length:.2f}")
print(f"Side of Square: {side:.2f}")
print(f"Area of Square: {area:.2f}")
