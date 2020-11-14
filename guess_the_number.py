#guess the number game
#version 1.0:

import random
import time

def getInput():
    try:
        userInput = int(input("Please Enter a Number between 1 and 100"))
    except ValueError:
        print ("Pls Input an Integer Value")
        main()
    return userInput

def genRandom():
    randomNumber = random.randint(0, 100)
    return randomNumber

def compareInput(userInput, genNumber):
    if userInput == genNumber:
        return "correct"
    else:
        return "incorrect"

def checkDiff(userInput, genNumber):
    if userInput > genNumber:
        return "Number is too high"
    elif userInput < genNumber:
        return "Number is too low"
    elif userInput == genNumber:
        return "Perfect"
    elif userInput >= genNumber-10 and userInput < genNumber:
        return "Almost There"
    

def main():
    randomNumber = genRandom()
    print ("Guess The Number Game")
    userInput = getInput()

    compare = compareInput(userInput, randomNumber)
    print (compare)
    print(checkDiff(userInput, randomNumber))
    
    while compare == "incorrect":
        userInput = getInput()
        compare = compareInput(userInput, randomNumber)
        print(compare)
        print(checkDiff(userInput, randomNumber))
    else:
        print ("Exiting Game")
        time.sleep(20)

main()
    
    
