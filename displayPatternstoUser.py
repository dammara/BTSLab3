# Markhus Dammar
# 20 September 2021
# this program will take user input to display a cool number pattern

pattern = "\t[{}]\n[{}] [{}] [{}]\n\t[{}]"


def display_pattern(number):
    print(pattern.format(number, number, number, number, number, number, number, number, number, number))


start = int(input("What number would you like to start at? (0-10) >>>"))
end = int(input("What number would you like to end at? (0-10) >>>"))

while start >= end or end >= 10:
    print("Please enter a value within the range")
    start = int(input("What number would you like to start at? (0-10) >>>"))
    end = int(input("What number would you like to end at? (0-10) >>>"))

for i in range(start, end):
    if i % 2 == 0:
        display_pattern('\033[33m' + str(i))
    else:
        display_pattern('\033[34m' + str(i))
