print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇

message = ''
a1 = input("You're at a crossroad, where do you want to go? LEFT or RIGHT?\n").lower()

if a1 != "left":
    message = "You fall into an abyss. Game Over!"
else:
    a2 = input("You get to a river. Do you want to SWIM or WAIT for boat?\n").lower()
    if a2 != "wait":
        message = "You were attacked by an aligator. Game Over!"
    else:
        print("A boat comes along and takes you to the other side.")
        a3 = input(
            "You get to a temple and there are two doors RED, BLUE and YELLOW. Which door do you take?\n").lower()
        if a3 == "red":
            message = "Molten lava pours on you. Game Over!"
        elif a3 == "blue":
            message = "You are eaten by beasts. Game Over!"
        elif a3 == "yellow":
            message = "You found the treasure. You win!"
        else:
            message = "Wrong choice. Game Over!"

print(message)
