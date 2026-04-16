# Using float() instead of int() to allow for measurements with decimal points.
# This ensures accuracy for architectural calculations.
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = length * width

print(f"The area of your rectangle, as planned, is {area} square units.")