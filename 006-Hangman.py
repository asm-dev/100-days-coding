"""  

What does this program do?
**************************
This program emulates the classic hangman game.
It takes a word from the random "words" list, and generates the equivalent number of spaces to fill.
It calculates the lives available, and generates an empty list of letters.
It then goes into a loop that works as long as the user has any remaining live.
Lives run out as the user selects letters that aren't in the word (letter and word are compared using the compare_letter() function).
If the user enters the same letter more than once, meaning that it has already been entered previously, thay're notified and prompted to enter a letter.
Blank spaces are replaced by the appropriate letters when there's a match.
Once all the blanks have been filled in, and therefore the word guessed, the program ends.

"""  

# Potential further improvements/iterations
# *****************************************
# - Avoid using numerical values, whole words, etc. a single letter is what we need and can use
# - Add difficulty levels (e.g. by changing how many lives an user gets)
# - UI
# - Give the option to play again, keeping a counter of guessed words (without losing, losing, etc. There are several options here)
# - Gamification - reward the user when they've guessed a word
# - Avoid repetition of words, have a wider selection 
# - Review if the program could be improved with functions, OOP, etc.
# - The "end" if/else could be added to the while loop
# - Polish a few details details, such as the way in which the list of letters already used is displayed, the texts syntax, etc.
 

import random
from functions import letter_finder

words = ["apple", "house", "cup", "eagle", "posture", "colours", "clock"]
word = random.choice(words).upper()
white_spaces = "_" * len(word)

lives = len(word)*2
letters = []

print(f"You've got {lives} lives. The word you have to guess has {len(word)} letters.\n\n{white_spaces}\n")

while lives > 0:

    # We ask the user to guess a letter
    letter = input("Try to guess a letter: ").upper()

    # We avoid the use of previously used letters
    while letter in letters:
        letter = input(f"\nPlease introduce a letter that isn't included in: {letters}, you've already used {letter} ").upper()
    letters.append(letter)

    # We check out if the letter guessed by the user is in the word
    index_letter = letter_finder(word, letter)

    # If the letter isn't in the word, the user gets notified and they lose a live 
    if index_letter == []:
        lives -= 1 
        print(f"\nThe letter {letter} isn't in the word. You have {lives} remaining lives.\n")
        # The game ends here if lives is not > 0

    # If the letter is in the word, we update and display "white spaces", which shall show the letters of the word that the user has guessed so far
    else:
        for i in index_letter:
            white_spaces_list = list(white_spaces)
            white_spaces_list[i] = letter
            white_spaces = ''.join(white_spaces_list)
        print(f"\n{white_spaces}\n")    
    
    # If the word has already been guessed fully (white_spaces == word) then the game ends
    if white_spaces == word:
        break

# We let the user know that the game has ended and why - they have either won or lost
if lives == 0:
    print("You have run out of lives. You've lost :(")
else:
    print("Congrats! You've guessed the word :)")
