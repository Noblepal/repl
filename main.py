#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator")

total = float(input("What was the total bill? "))
percent = float(input("What pecent would you like to give? 10, 12 or 15? "))
num_people = float(input("How many people split the bill? "))

increment = percent / 100 * total
grand_total = total + increment

individual_amount = grand_total / num_people
# Python format
final_amount = "{:.2f}".format(individual_amount)

print(f"Each person should pay: {final_amount}")