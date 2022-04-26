# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

bmi = float(weight) / (float(height) ** 2)
str_bmi = ""

if bmi < 18.5:
    str_bmi = "underweight"
elif bmi < 25:
    str_bmi = "normal weight"
elif bmi < 30:
    str_bmi = "overweight"
elif bmi < 35:
    str_bmi = "obese"
else:
    str_bmi = "clinically obese"

bmi = "{:.1f}".format(bmi)

print(f"Your BMI is {bmi}, you are {str_bmi}")
