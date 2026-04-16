# A nested if statement creates a second layer of choice.
# The 'swim' question only appears if the user chooses 'left' first.
path = input("Do you go 'left' or 'right'? ").lower()

if path == "left":
    choice = input("You see a river. Do you 'swim' or 'wait'? ").lower()
    if choice == "swim":
        print("You found a submerged treasure chest! You win!")
    else:
        print("You waited too long. A monster caught you!")
else:
    print("You fell into a pit on the right path. Game over.")
