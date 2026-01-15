import random
target=random.randint(1,100)
while True:
    userChoice=input("Guess the Target and Quit(Q):")
    if(userChoice=="Q"):
        break
    userChoice=int(userChoice)
    if(userChoice==target):
        print("Success: Correct Guess")
        break
    elif (userChoice<target):
        print("Your number is Too small.Take a Bigger Guess")
    else:
        print("Your number is Too big.Take a smaller Guess")

        
print("----------------Game Over-----------------")
