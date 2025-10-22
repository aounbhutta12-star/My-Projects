import random

while True:
    n = input("Roll The Dice (y/n): ").lower()

    if n == "y" or n == "yes":
        print(f"Your number is ({random.randint(1,10)}, {random.randint(1,10)})")

    elif n == "n" or n == "no":
        print("Thank You!")
        break   # this stops the while loop

    else:
        print("Invalid input!")



#SUMMARY
        # the reason i used while so idont need to run the program again and again
        #now if user enter' y ' the program will run again after the output 
        #if we say " n " we used break after the elif so the program will not run