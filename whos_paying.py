import random
"""
participants = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]

random_participants = random.choice(participants)

print(f"{random_participants} is going to buy the meal today!")


############
names_string = input("Give me everybody's names, seperated by a comma. ")

names = names_string.split(", ")

random_name = random.choice(names)

print(f"{random_participants} is going to buy the meal today!")
"""
#############
names_string = input("Give me everybody's names, seperated by a comma. ")

names = names_string.split(", ")

num_items = len(names)

random_choice = random.randint(0, num_items -1)

person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to buy the meal today!")

