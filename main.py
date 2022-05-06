import random

rock = "🪨"
paper = "📄"
scissors = "✂"

options = [rock, paper, scissors]

choice = int(input("What do you choose?\n0: Rock\n1. Paper\n2. Scissors\n"))
computer_choice = random.randint(0, 2)

result = "The winner is: "

if 2 >= choice >= 0:
    if choice == 0:
        if computer_choice == 0:
            result += "Draw!"
        elif computer_choice == 1:
            result += "Computer!"
        else:
            result += "You!"
    elif choice == 1:
        if computer_choice == 0:
            result += "You!"
        elif computer_choice == 1:
            result += "Draw!"
        else:
            result += "Computer!"
    elif choice == 2:
        if computer_choice == 0:
            result += "Computer!"
        elif computer_choice == 1:
            result += "You!"
        else:
            result += "Draw!"
    else:
        result = "You didn't select a valid option"

    print(f"You chose: {options[choice]}")
    print(f"Computer chose: {options[computer_choice]}")

else:
    result += "Nobody!"
    print("Please select a valid option")

print(result)
