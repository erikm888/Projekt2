'''
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Erik Milošovič
email: erik.milosovic@gmail.com
discord: erik.m#9937
'''

import random
import time


def userInput():
    print("-----------------------------------------------")
    number = input("Enter a number:")
    print("-----------------------------------------------")
    # check input
    if not number.isnumeric():
        print("Inputted value not a number, try again")
        return userInput()
    elif number[0] == "0":
        print("Inputted number starts with 0, try again")
        return userInput()
    elif len(number) != 4:
        print("Inputted number is not 4 digits long, try again")
        return userInput()
    elif len("".join(set([i for i in str(number)]))) != 4:
        print("Inputted number contains duplicates, try again")
        return userInput()
    return int(number)


if __name__ == "__main__":
    print("""Hi there!
    -----------------------------------------------
    I've generated a random 4 digit number for you.
    Let's play a bulls and cows game.""")

    # Guessing
    playTime = time.time()
    guesses = 1
    randomNumber = 0
    while len("".join(set([i for i in str(randomNumber)]))) != 4:
        randomNumber = random.randint(1234, 9876)
    
    print(randomNumber)
    guessNumber = userInput()
    while randomNumber != guessNumber:
        bulls = 0
        cows = 0
        for i in range(4):
            if str(randomNumber)[i] == str(guessNumber)[i]:
                bulls += 1
            elif str(randomNumber)[i] in str(guessNumber):
                cows += 1
        print("{} bull{}, {} cow{}".format(bulls, "s" if bulls >
              1 else "", cows, "s" if cows > 1 else ""))
        guessNumber = userInput()
        guesses += 1

    print("Correct, you've guessed the right number in {} guesses!".format(guesses))
    print("It took you {} seconds".format(round(time.time() - playTime, 2)))

    # Store statistics
    try:
        with open("statistics.txt", mode="r", encoding='utf-8') as f:
            # read the fist line number
            nPlays = int("".join(i for i in f.readline() if i.isdigit()))
            avgTries = float("".join(i for i in f.readline() if i.isdigit() or i == "."))
            
            nPlays += 1
            print(nPlays)
            print(avgTries)
            print(avgTries * (nPlays - 1))
            avgTries = (avgTries * (nPlays - 1) + guesses) / nPlays
            
            print("Number of plays: {}".format(nPlays))
            print("Average number of tries: {}".format(avgTries))
    except:
        print("You are the first player, there are no statistics yet")
        nPlays = 1
        avgTries = guesses

    with open("statistics.txt", mode="w", encoding='utf-8') as f:
        f.write("Number of plays: {}\nAverage number of tries: {}".format(
            nPlays, avgTries))
