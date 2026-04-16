#Python
# The if-elif-else structure allows for multiple checks in a sequence.
# Once one condition is met, the rest are ignored.
score = int(input("Enter your exam score (0-100): "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: Needs Improvement")
