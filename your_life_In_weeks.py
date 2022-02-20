age = input("What is your current age:")

age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remainnig = years_remaining * 12

message = f"You have {days_remaining}, {weeks_remaining} weeks, and {months_remainnig} moths left"

print(message)