# A text adventure using functions to represent different world locations.
def enchanted_forest():
    print("You are in a glowing forest. Do you 'climb' a tree or 'follow' a fairy?")
    choice = input("> ").lower()
    if choice == "climb":
        print("You see the whole kingdom. Victory ending!")
    else:
        print("The fairy leads you into a trap. Game Over.")

def dragon_cave():
    print("A dragon sleeps here. Do you 'steal' the gold or 'sneak' out?")
    choice = input("> ").lower()
    if choice == "steal":
        print("The dragon wakes up! Crispy ending...")
    else:
        print("You escaped safely. Survival ending!")

print("Choose your path: 'forest' or 'cave'?")
path = input("> ").lower()
if path == "forest":
    enchanted_forest()
else:
    dragon_cave()
