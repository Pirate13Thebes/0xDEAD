# Logical operators like 'and' allow us to check multiple requirements at once.
# Both conditions must be True for the person to enter.
age = int(input("How old are you? "))
gold = int(input("How much gold do you have? "))

if age >= 18 and gold >= 20:
    print("The bouncer moves aside. Welcome to the club!")
else:
    print("You do not meet the requirements. Access Denied.")

