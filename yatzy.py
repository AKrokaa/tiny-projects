import numpy as np
import time
import sys

currentRoll = []
numbers = [1, 2, 3, 4, 5, 6]

def startGame():
    global score 
    score = 0

def totalScore(x):
    sum = x * currentRoll.count(x)
    global score
    score = score + sum
    numbers.remove(x)
    print("This is your current score:", score)
    if len(numbers) == 0:
        print("You've finished all of the numbers!")
        if score >= 63:
            score = score + 50
            print("Your final score is: ", score, "!")
            currentRoll.clear()
        else:
            print("Your final score is: ", score, "!")
            currentRoll.clear()
    else:
        currentRoll.clear()
        userInput()

def checkTotalScore():
    print(score)

def dice(x):
    currentRoll.append(x)

def chooseNumber():
    for numbers2 in range(5 - len(currentRoll)):
        dice(np.random.randint(1, 7))
    print("This is remaining dice", currentRoll)
    userInput = int(input("""
Where do you want to add your dice score?
1 - Ones        4 - Fours
2 - Twos        5 - Fives
3 - Threes      6 - Sixes
    
CHOOSE HERE = """))
    if userInput in numbers:
        totalScore(userInput)
    else:
        print("You've already chosen that one! Try again")
        chooseNumber()

def roll():
    for i in range(2):
        for numbers in range(5 - len(currentRoll)):
            dice(np.random.randint(1, 7))
        print(currentRoll)
        userInputRoll()
    chooseNumber()

def userInput():
    print("""
     Welcome to Yatzy!
###########################
Pick one of the following:
- roll      - score
- help      - left over (numbers)
        """)

    userAnswer = str(input("What do you want to do?\n= "))
    if (userAnswer == "score"):
        checkTotalScore()
        userInput()
    elif userAnswer == "roll":
        roll()
    elif userAnswer == "help":
        print("""
This is Yatzy!
You roll five dice three times!
Between each roll you get to pick which dice you want to discard.
The amount of discarded dice gets rolled again!
""")
        time.sleep(3)
        userInput()
    elif userAnswer == "numbers":
        print("These are the remaining numbers left to roll for:\n= ", numbers)
        time.sleep(2)
        userInput()
    elif userAnswer == "reset":
        resetGame()
        userInput()
    else:
        userInput()

def resetGame():
    print("Are you sure?:")
    resetInput = userInput("y/n = ")
    if resetInput == "y":
        global numbers
        global score
        numbers = [1, 2, 3, 4, 5, 6]
        score = 0
        userInput()
    elif resetInput == "n":
        userInput()
    else:
        print("Please input either y/n")
            
def userInputRoll():
    askAboutRemove = input("Do you want to remove any dice?\n y/n = ")
    if askAboutRemove == "y":
        amountRemoveDice = int(input("How many dice do you want to remove\n 1 - 5 = "))
        for i in range(amountRemoveDice):
            removeDice = int(input("Which dice do you want to remove? (Input the position from last to first, separated by ENTER)\n= ")) #Error hvis man går fra lavest til størst
            if removeDice <= 6 and removeDice >= 1:
                currentRoll.pop(int(removeDice - 1))
                removeDice -= i
            else:
                print("That dice doesn't exist, try again")
                userInputRoll()
        print("These are the remaining dice:", currentRoll)
        return currentRoll

    elif askAboutRemove == "n":
        chooseNumber()

    else:
        print("Choose one of the of the options, y/n")
        userInputRoll()

def endGame():
    endgame = input("Do you want to play again?\ny/n = ")
    if endgame == "y":
        resetGame()
    if endgame == "n":
        print("\nGoodbye!")
        time.sleep(1)
        sys.exit()

startGame()
userInput()

while True:
    try:
        break
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("Next entry.")
        print()
        break