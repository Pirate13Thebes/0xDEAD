# quest_26_simple_calculator.py

# Step 1: Define functions (must be at the top)
def add(a, b): 
    return a + b

def subtract(a, b): 
    return a - b

def multiply(a, b): 
    return a * b

def divide(a, b): 
    if b == 0:
        return "Error: Division by zero"
    return a / b

# Step 2: Get user input
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Choose operation (add, subtract, multiply, divide): ").lower()

    # Step 3: Route to the correct function
    if operation == "add":
        print(f"Result: {add(num1, num2)}")
    elif operation == "subtract":
        print(f"Result: {subtract(num1, num2)}")
    elif operation == "multiply":
        print(f"Result: {multiply(num1, num2)}")
    elif operation == "divide":
        print(f"Result: {divide(num1, num2)}")
    else:
        print("Invalid operation selected.")

except ValueError:
    print("Error: Please enter valid numbers.")