# Build my own version of Wordle

import numpy as np
import random

# Load list of 5-letter words
word_list = np.array(np.loadtxt('./sgb-words.txt', dtype='str'))

# Choose the word to guess randomly
wordle = word_list[random.randint(1, len(word_list))]
# print(wordle)

guess_count = 0
# Take user's guess
while guess_count < 6:
    correct_spot = []
    wrong_spot = []
    last_guess_output = []
    if guess_count >= 1:
        print(f'\nYour last guess was {user_guess}. {last_guess}')
        user_guess = str(input(f'Enter your next guess: '))
    else:
        user_guess = str(input('Enter your guess: '))
    guess_count += 1
    if user_guess not in word_list:
        guess_count -= 1
        print('That is not a word.')
        continue
    for letter in user_guess:
        if wordle[user_guess.index(letter)] == letter:
            correct_spot.append(letter)
            last_guess_output.append(letter.upper())
        elif wordle[user_guess.index(letter)] != letter and letter in wordle:
            wrong_spot.append(letter)
            last_guess_output.append(letter)
        else:
            last_guess_output.append('_')
    if user_guess == wordle:
        print(f'Congratulations! The wordle was {wordle}. You won!')
        break
    last_guess = ''.join(last_guess_output)
    # print(f'These letters are in the correct spot: {correct_spot}.')
    # print(f'These letters are in the wrong spot: {wrong_spot}.')

if guess_count == 6:
    print(f'Sorry, you didn\'t guess the wordle within 6 tries. The wordle was {wordle}.')
