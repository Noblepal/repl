# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split(',')
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇

height_sum = 0
for height in student_heights:
    height_sum += height

students_count = 0
for height in student_heights:
    students_count += 1

average = height_sum / students_count

print(f"The average height of the class is: {round(average)}")
