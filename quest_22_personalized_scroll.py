# Parameters act as placeholders for information the function needs to work.
# This makes the function flexible for any user name or quest.
def personalized_greeting(name, quest):
    print(f"Greetings, {name}! Your noble quest for {quest} is legendary.")

# Asking for user input and passing it as arguments to the function.
user_name = input("Enter your name: ")
user_quest = input("What is your quest? ")

personalized_greeting(user_name, user_quest)
