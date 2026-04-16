# Using an 'if' statement inside a 'for' loop allows us to filter data.
# We use the modulo operator (%) to check if a number is divisible by 2.
print("Foraging for even numbers between 1 and 20:")

for number in range(1, 21):
    if number % 2 == 0:
        print(f"Found an even number: {number}")
