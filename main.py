# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# 365 days in a year
# 52 weeks in a year
# 12 months in a year

years_remaining = 90 - int(age)

days = round(years_remaining * 365)
weeks = round(years_remaining * 52)
months = round(years_remaining * 12)

message = f"You have {days} days, {weeks} weeks and {months} months left till 90yrs."
print(message)