
# This is a Python script of the classic game “Hangman”.
# The word to guess is represented by a row of dashes.
# If the player guess a letter which exists in the word, the script writes it in all its correct positions.



import random
import string

from words import words

# to get a random word
def get_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


#main game - hangman

def hangman():
    word = get_word(words)
    word_letters = set(word)                    # all the letters in the word stroed as set as it stores a unique occurence of character present
    alphabet = set(string.ascii_uppercase)      # contains all the alphabets in the uppercase
    used_letter = set()

    #take user input

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        #letters already used
        print('You have ', lives,' lives left and you have used these letters : ', " ".join(used_letter))

        #what current word is (ie W-R-)
        word_list = [letter if letter in used_letter else '-' for letter in word]
        print("Current word : ",' '.join(word_list))

        user_letter = input("Guess a letter - ").upper()
        if user_letter in alphabet - used_letter:
            used_letter.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1       # take away one live if the answer is wrong
                print("Letter is wrong")

        elif user_letter in used_letter:
            print("Letter already used!!! ")

        else:
            print("Invalid character!!!")

    #reaches when word is predicted or lives ended
    if lives==0:
        if len(word_letters) > 0:
            print("You died, sorry. The word was ",word)
        else:
            print("You guessed the word,",word)
    else:
        print("You guessed the word,", word)



hangman()




