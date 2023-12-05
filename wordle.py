import numpy as np
import random
import os

def wordle():

    #Opening a txt file with the english dictionary, turning it into a numpy array
    filepath = os.getcwd()+"\Wordle\sgb-words.txt"
    wordlistFile = open(filepath)
    fiveLetterWords = np.array(wordlistFile.readlines())
    
    #wordToday chooses a random five letter word. That is today's word
    wordToday = random.choice(fiveLetterWords)

    #Initiating a counter that will keep track of how many times the user has guessed
    counter = 0

    #Printing nice things that people like to read when they start a game
    print("Welcome to Wordle! Here's how to play:",flush=True)
    print("------------",flush=True)
    print("0: This letter does not match. (grey)",flush=True)
    print("?: This letter exists somewhere in the word, but not here. (yellow)",flush=True)
    print("!: This letter is in the correct spot. (green)",flush=True)
    print("------------",flush=True)
    print("Enter a five-letter guess as an input during your turn.",flush=True)
    print("------------",flush=True)
    print("Type 'end' to stop playing")
    print("------------",flush=True)

    #Starting the while loop in which the majority of the game runs
    while True:
        
        #This while loop initiates the input request at the beginning of each turn
        while True:

            #Your guess
            guess = input()

            #After the user types a guess, this checks if the guess is "end", which will stop the loop and then later stop the whole game
            if guess == "end":
                break

            #Check if the user inputted a five-letter word. If not, tell the user about their mistake and prompt for an input again
            if len(guess) != 5:
                print("Please type a five-letter word",flush=True)
                print("------------")
            else:
                break
        
        #Now, after checking one more time if the input is "end", the game will stop
        if guess == "end":
            break

        #Initialize a status variable storing each letter's status. Initialized with all greens
        status = np.array(["0","0","0","0","0"])

        #Check the guess against today's word for imperfect matches
        for n in range(5):
            if wordToday.find(guess[n]) != -1:
                status[n] = "?"

        #Check the guess against today's word for perfect matches
        for n in range(5):
            if guess[n] == wordToday[n]:
                status[n] = "!"

        #Print the results of the user's guess
        print(status[0]+status[1]+status[2]+status[3]+status[4],flush=True)
        print("------------")

        #Add one to the guess counter
        counter += 1
        
        #Check if the user inputted the correct word for today. If they did, say they won and end the program
        if status[0] == "!" and status[1] == "!" and status[2] == "!" and status[3] == "!" and status[4] == "!" :
            print("YOU WIN!!!",flush=True)
            print("--- Game made by Ziggy ---")
            break

        #Check if the user has made six guesses. If they have, print the corresponding loss statements. This does not actuate if the user won on their last guess
        if counter == 6:
            print("YOU LOST :(",flush=True)
            print("The word was:",flush=True)
            print(wordToday,flush=True)
            print("--- Game made by Ziggy ---")
            break

wordle()