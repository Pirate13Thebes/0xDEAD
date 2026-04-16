# Implementing attempt-based logic using a loop and a boolean flag.
secret_code = "42"
attempts = 3
success = False

print("System Locked. Enter the 2-digit override code.")

for i in range(attempts):
    guess = input(f"Attempt {i+1}/3: ")
    if guess == secret_code:
        print("Access Granted. Welcome back, Admin.")
        success = True
        break
    else:
        print("Incorrect code.")

if not success:
    print("Lockdown initiated. Too many failed attempts.")
