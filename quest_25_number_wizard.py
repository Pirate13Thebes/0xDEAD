# Level 6: The Grand Challenge
# This script improves the guessing game by providing directional feedback.
secret_number = 42
guess = 0

print("Welcome to the Number Wizard's tower!")

while guess != secret_number:
    guess = int(input("Guess the secret number: "))
    
    if guess < secret_number:
        print("Too low! The magic energy is higher.")
    elif guess > secret_number:
        print("Too high! Lower your expectations.")
    else:
        print("Correct! You are a true Number Wizard.")
