# Nested lists exercise

row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]
row4 = ["⬜", "⬜", "⬜"]
treasure_map = [row1, row2, row3, row4]
print(f"{row1}\n{row2}\n{row3}\n{row4}")
position = input("Where do you want to hide the treasure? ")

# Add this to the selected position 🟥
horiz = int(position[0]) - 1
vert = int(position[1]) - 1

treasure_map[vert][horiz] = "🟥"

print(f"{row1}\n{row2}\n{row3}\n{row4}")
