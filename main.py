# Add all the numbers from 1 to 100

# With step
# for n in range(0, 11, 3):
#     print(n)
#
# total = 0
# for number in range(1, 101):
#     total += number
#
# print(total)

# Exercise adding even numbers in the range 1-100

even_sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        even_sum += i

print(even_sum)

# OR - using step

even_sum2 = 0
for i in range(2, 101, 2):
    even_sum2 += i

print(even_sum2)
