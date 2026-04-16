# A Master Spell involves passing the output of one function into another.
# This is the basis of building complex systems from simple parts.
def ask_for_age():
    return int(input("How many years have you lived? "))

def can_they_vote(age):
    if age >= 18:
        print("The Oracle grants you the right to vote!")
    else:
        print("The Oracle says you are too young to vote.")

# We call the first function and pass its returned value directly to the second.
current_age = ask_for_age()
can_they_vote(current_age)
