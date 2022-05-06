import random

names_string = input("Give me everybody's names, separated by a comma: ")

names = names_string.split(", ")

print(f"Candidates: {names}")

num_people = len(names)

random_number = random.randint(0, num_people - 1)

print(f"{names[random_number]} will be paying the bill!")

# Using random.choice()
person_to_pay = random.choice(names)
print(f"Random person to pay: {person_to_pay}")

