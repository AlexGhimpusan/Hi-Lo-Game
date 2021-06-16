#imports
import random
import os

#function to clear the console
clear = lambda: os.system('cls')

#the guess will be held between 1 and this number
maxNumber = 20

#randomzirer between 1 and a max value
def randomize(maxValue):
    x = int(random.randint(1, maxValue))
    return x

#hint function for greater or smaller values
def hint(randomNumber, inputNumber):
    #Greater or Smaller
    if randomNumber > inputNumber:
        print("My number is greater")
    elif randomNumber < inputNumber:
        print("My number is smaller")

#game function
def Round():
    randomNumber = randomize(maxNumber)
    roundScore = 50
    print("\nI'm thinking about a number between 1 and " + str(maxNumber))

    while not roundScore == 0:
        print("\nThis round score: " + str(roundScore) + "p")

        #user inputs
        try:
            inputNumber = int(input("Enter your guess: "))
        except:
            print("The value MUST be an integer.")
            continue
        
        #WIN condition
        if randomNumber == inputNumber:
            break
        else:
            #hints if inputs are wrong
            hint(randomNumber, inputNumber)
            roundScore -= 10

    if roundScore == 0:
        print("\n!!!Round over. This round score reached 0")
        print("My number was " + str(randomNumber))
    else:
        print("\n!!!Congratulations! The computer number was " + str(randomNumber))
        print("You win " + str(roundScore) + "points")

    return roundScore

def Game():
    print("****************************************************************")
    print("Your mission is to guess the number.")
    print("After every wrong guess we will give you a hint: if the computer's number is greater or smaller than your guess.")
    print("With every wrong guess your score will decrease with 10p until 0.")
    print("If the score reaches 0 the game is over")
    print("Good Luck!")
    print("****************************************************************")

    #a player score
    playerScore = 0

    answer = "y"
    while answer.lower() == "y":
        print("\n\t\t\t\t\t\tYour current score: " + str(playerScore))
        roundScore = Round()
        playerScore += roundScore
        answer = input("\nDo you want to play again? Y or N: ")
        if answer.lower() == "y":
            clear()
    print("\n!!!Your final score is: " + str(playerScore))
    input("Press ENTER to quit the game...")

Game()