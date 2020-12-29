
import random

def hangman(winning_word, char_guessed):
    for letter in winning_word:
        if letter in char_guessed:
            print(f' {letter} ', end='')  #print(letter)
        else:
            print(' __ ', end='') #print(" __ ")
    print()

def over(winning_word, char_guessed):
    counts = 0
    for letter in set(winning_word):
        if letter in char_guessed:
            counts += 1
    return counts == len(set(winning_word))


words = ['random', 'choice', 'beautiful', 'alphabet', 'objective', 'intelligent', 'hamilton', 'instagram', 'mountain', 'laptop']
random.shuffle(words)
winning_word = random.choice(words)
char_guessed = ''

print("The word has " + len(winning_word) + " letters.")
user_guess = input("Please enter a letter. ").lower()[0]

while True:
    if (user_guess in winning_word) and (user_guess not in char_guessed):
        print("You got it right! " + user_guess + " is in the word!")
        char_guessed += user_guess  #char_guessed = char_guessed + user_guess
        hangman(winning_word, char_guessed)
        game_over = over(winning_word, char_guessed)
        if game_over == True:
            print("Congratulations! You guessed the word! " + winning_word.upper())
            break
        else:
            user_guess = input("Please guess another letter! ")

    elif (user_guess not in winning_word):
        print("That letter is not in the word. ")
        user_guess = input("Please guess another letter! ")



