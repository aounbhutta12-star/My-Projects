import random

while True:
    try:    
        user = input("Rock, Paper, Scissors? (r, p, s): ").lower()

        computer = random.choice(["r", "p", "s"])
    
        userdict = {
            "rock": "r",
            "paper": "p",
            "scissors": "s"
        }

        reversedict = {
            "r": "Rock",
            "p": "Paper",
            "s": "Scissors"
        }

  
        if user in ["r", "p", "s"]:
            you = user
        else:
            you = userdict[user]

        print(f"You guessed {reversedict[you]} and the computer guessed {reversedict[computer]}")

        if you == computer:
            print("It's A Draw")
        elif (you == "r" and computer == "s") or (you == "p" and computer == "r") or (you == "s" and computer == "p"):
            print("You Won")
        else:
            print("Computer Won")

    except KeyError:
        print("Enter A Valid Character")
