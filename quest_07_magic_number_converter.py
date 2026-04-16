# The input() function always returns a string (text).
# I am using int() to convert that text into a number so I can subtract it from the current year.
birth_year_str = input("What year were you born? ")
birth_year = int(birth_year_str)

current_year = 2026
age = current_year - birth_year

print(f"Since you were born in {birth_year}, you are approximately {age} years old.")
