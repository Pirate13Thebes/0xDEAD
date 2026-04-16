# This while loop relies on user input to break the cycle.
# The loop will keep asking until the user provides the correct secret number.
secret_number = 42
guess = 0

while guess != secret_number:
    guess = int(input("Guess the secret number to break the loop: "))
    if guess != secret_number:
        print("That is not the secret number. Try again!")

print("Correct! The loop is finally broken.")
