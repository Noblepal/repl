# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

combined_names = name1 + name2
combined_names = combined_names.lower()

t1 = combined_names.count("t")
r1 = combined_names.count("r")
u1 = combined_names.count("u")
e1 = combined_names.count("e")

true1 = t1 + r1 + u1 + e1

l2 = combined_names.count("l")
o2 = combined_names.count("o")
v2 = combined_names.count("v")
ee2 = combined_names.count("e")

love1 = l2 + o2 + v2 + ee2

score_int = int(str(true1) + str(love1))

message = ''

if score_int < 10 or score_int > 90:
    message = "you go together like coke and mentos"
elif score_int >= 40 and score_int <= 50:  # Could be simplified to 40 <= score_int <= 50
    message = "you are alright together"

print(f"Your score is {score_int} {message}")
