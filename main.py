# num_char = len(input("What is your name?"))

# #Type checking
# print(type(num_char))

# #Type conversion
# str_num_char = str(num_char)

# print("Your name has "+ str_num_char + " characters")

# a = 123
# float_num  = float(a)
# print(float_num)

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

print(type(two_digit_number))

a = two_digit_number[0]
b = two_digit_number[1]

print(int(a) + int(b))