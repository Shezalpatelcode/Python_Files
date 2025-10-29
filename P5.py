# Bitwise operations example
val = 0xCAFE

# 1. Test if at least three of last four bits are ON
test = bin(val & 0xF).count("1") >= 3
print("At least three of last four bits ON:", test)

# 2. Reverse the byte order (0xCAFE -> 0xFECA)
reversed_val = ((val & 0xFF) << 8) | ((val >> 8) & 0xFF)
print(f"Reversed byte order: 0x{reversed_val:04X}")

# 3. Rotate 4 bits right (0xCAFE -> 0xECAF)
rotated = ((val >> 4) | (val << 12)) & 0xFFFF
print(f"Rotated 4 bits right: 0x{rotated:04X}")
