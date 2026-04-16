# The 'return' keyword sends a value back to where the function was called.
# This allows us to use the result of a calculation in our main code.
def calculate_area(length, width):
    return length * width

# Calling the function for two different rectangles and storing/printing results.
area_1 = calculate_area(10, 5)
area_2 = calculate_area(15.5, 4)

print(f"The first rectangle area is {area_1}.")
print(f"The second rectangle area is {area_2}.")
