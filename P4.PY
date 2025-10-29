# Input: measurement in inches
inches = float(input("Enter measurement in inches: "))

# Conversions
feet = inches / 12
yards = inches / 36
centimeters = inches * 2.54
meters = inches / 39.37

# Display results
print(f"\nEquivalent measurements:")
print(f"Feet: {feet:.2f} ft")
print(f"Yards: {yards:.2f} yd")
print(f"Centimeters: {centimeters:.2f} cm")
print(f"Meters: {meters:.2f} m")
