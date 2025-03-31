print("Welcome to the number guess game. Guess a number between 1 to 50.")
import random
computerchoice = random.randint(1,50)
if computerchoice%2==0:
    print("Hint : Computer guess is even.")
else:
    print("Hint : The computer guess is odd")
userguess=int(input('enter your guess :'))
if userguess <1 or userguess> 50:
    print(
        "Please enter value between 1 to 50."
    )
elif userguess ==computerchoice:
    print("Welldone you did it ! ")
else:
    print("Try again.")
    print("The computer guess was : ",computerchoice)