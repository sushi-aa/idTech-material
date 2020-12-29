#credit: https://github.com/ProgrammerRaj-py/Hangman/blob/master/hangman.py

# Importing Libraries
import random

# function
def hangman(winning_word, char_guessed):
    for i in winning_word:
        if i in char_guessed:
            print(f' {i} ', end='')
        else:
            print(' __ ', end='')
    print()


def over(winning_word, char_guessed):
    counts = 0
    for i in set(winning_word):
        if i in char_guessed:
            counts += 1
    return counts == len(set(winning_word))


# Word
words = []
fileObj = open('hangman_wordlist.txt')
words = fileObj.read().split()
print(words)

random.shuffle(words)
winning_word = random.choice(words)
char_guessed = ''

# main
print(f'The word has {len(winning_word)} characters.\n')
user_guess = input('Guess any character: ').lower()[0]
counter = 1
while True:

    if user_guess in char_guessed:
        user_guess = input('Already guessed.\nGuess again: ')
        '''
        counter = counter + 1
        if counter > 3:
            break;
        '''

    elif (user_guess in winning_word) and (user_guess not in char_guessed):
        print(f'Yes! "{user_guess}" is in the word.')
        char_guessed += user_guess
        hangman(winning_word, char_guessed)
        game_over = over(winning_word, char_guessed)
        if game_over:
            print(f'\nCongrats. You guessed the word "{winning_word.upper()}".')
            break
        else:
            user_guess = input('Guess next character: ')
            '''
            counter = counter + 1
            if counter > 3:
                break;
            '''


    elif user_guess not in winning_word:
        print(f'Sorry. "{user_guess}" is not in the word.')
        user_guess = input('Guess again: ')
        '''
        counter = counter + 1
        if counter > 3:
            break;
        '''
