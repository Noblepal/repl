print("Welcome to the roller-coaster!")
height = int(input("What is your height in cm? "))
price = 0

if height >= 120:
    print("You can ride the roller-coaster!")
    age = int(input("What is your age?"))
    if age <= 12:
        price = 5
        print(f"Child tickets: ${price}")
    elif age <= 18:
        price = 7
        print(f"Youth tickets: ${price}")
    else:
        price = 12
        print(f"Adult tickets: ${price}")

    wants_photo = input("Do you want a photo taken? Y or N ")

    if wants_photo == 'y':
        price += 3

    print(f"Your bill is: ${price}")

else:
    print("You are too short to ride the roller-coaster!")
