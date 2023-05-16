# Ranges in python

# Creates a range of numbers between the pair specified
# This will make the loop go number by number
for number in range(1, 11):
    print(number)

# Adding a third param will make the loop go in that amount of steps at a time
for number in range(1, 11,  3):
    print(number)


total = 0
for number in range(1, 101):
    total += number
print(total)