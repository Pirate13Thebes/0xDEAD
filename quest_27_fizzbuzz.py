# FizzBuzz is a classic logic test.
# The order of the if-statements is crucial; multiples of 15 must be checked first.
for i in range(1, 101):
    # Check if divisible by both 3 and 5
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
