print("Welcome to the roller-coaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the roller-coaster!")
    age = int(input("What is your age?"))
    if age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("You CANNOT ride the roller-coaster!")
