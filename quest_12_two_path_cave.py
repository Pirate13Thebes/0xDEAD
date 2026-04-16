# The if-else statement handles both the 'True' and 'False' outcomes.
# It ensures the program always has a path to follow.
secret_password = "DragonFire"
user_entry = input("Whisper the secret password to enter the cave: ")

if user_entry == secret_password:
    print("The stone door rumbles open... Access Granted!")
else:
    print("The guardian glares at you... Access Denied!")