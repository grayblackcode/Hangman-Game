import random
import string

words = ['coffee', 'approach', 'advance', 'message', 'edition', 'attachment', 'receipt', 'mouth', 'degree', 'license',
         'retreat', 'concert', 'acquaintance', 'measure', 'kitchen', 'pool', 'chain', 'swell', 'call', 'crash', ]

word = random.choice(words)


guessed_word = ['_' for char in word]
print(' '.join(guessed_word), '\n')
final_word = ' '.join(word)

lst_word = list(word)
rounds = 6
# create an empty list to add guessed letter to if it's in the word
is_part_of = []

# a list of all the available letters to restrict user input to unused lowercase letters only
letters = string.ascii_lowercase
available_letters = []
for x in letters:
    available_letters.append(x)
print(','.join(available_letters))

while rounds:
    try:
        guess = input('\nGuess a letter: ')
        available_letters.remove(guess)

        # cehck to see if letter guessed is correct
        for i in range(len(lst_word)):
            if lst_word[i] == guess:
                is_part_of.append(True)
                guessed_word[i] = guess
            else:
                is_part_of.append(False)

        # if not correct, less rounds by 1
        if True not in is_part_of:
            rounds -= 1
        # clear the array to be used in the next round
        is_part_of.clear()

        print(' '.join(guessed_word))

        # only print the available letters in this condition
        if ' '.join(guessed_word) != final_word:
            print('\nAvailable Letters:\n', ','.join(available_letters))
            print(f'\n{rounds} Rounds left')
        else:
            pass

        if rounds > 0 and ' '.join(guessed_word) == final_word:
            print('\nYou Won!')
            break
        elif rounds == 0 and ' '.join(guessed_word) != final_word:
            print('You Lost!', '\nThe word is: ', final_word)

    except ValueError:
        print("Error! Only one letter from \"Available Letters\" allowed!")

