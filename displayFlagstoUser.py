# Markhus Dammar
# 20 September 2021
# This program takes user input to print a flag


star = input("""Which stars would you like to use? \nPlease copy and paste a star"
             \n★', '☆', '⭐', '✯' \n>>> """)

stripe = input("Which stripe would you like to use? \n- , _ , = \n>>> ")
num_flags = int(input("how many flags do you want? >>> "))
flag = (((f"{star}" * 13 + f"{stripe}" * 16 + "\n" + f"{star}" * 14 + f"{stripe}" * 15 + "\n") * 2) + (f"{stripe}" * 37 + "\n") * 3)

for num_flags in range(0, num_flags):
    print(flag)
