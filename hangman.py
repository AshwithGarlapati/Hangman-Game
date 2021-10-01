import random


def get_attempts():
    # To get number of attempts form the user and checking the attempts are in the range of 1 to 25.
    attempts = int(input('\nHow many number of incorrect attempts do you need[1-25]? '))
    if attempts > 25 or attempts < 1:
        print('{} is not an integer between 1 and 25\nPlease select an integer between 1 and 25.'.format(attempts))

    return attempts


def get_word_length():
    # Getting the word length from the user an checking weather the length is in the range 4 to 16.
    length = int(input('\nSelect the word length that is between [4-16] '))
    if length > 16 or length < 4:
        print('Please select the word length that is between 4 to 16')

    return length


# Starting of the execution of the program.
print('''Welcome to the game of HANGMAN...''')
# Getting number of attempts and word length.
no_of_attempts = get_attempts()
word_length = get_word_length()

# Opening the word fle file in read mode and reading all the words in the file and separating them into a string list.
f = open("words.txt.txt", "r")
all_text = f.read()
words = list(map(str, all_text.split()))

# Filtering the words that are of length equal to word length.
filtered_words = list(filter(lambda word: len(word) == word_length, words))
# Getting a random word from filtered word.
random_word = random.choice(filtered_words)

# Guessing of characters
print('\n\nGuess the character\'s: ')
print('-' * word_length)
char = ' '

# Generating a empty string of hyphens with length 16.
guess_word = list('-' * 16)


while no_of_attempts > 0:

    # Checking weather the character is present in random word and printing it.
    if char in random_word:
        for j in range(len(random_word)):
            if random_word[j] == char:
                print(char)
                guess_word[j] = char
            else:
                print(guess_word[j])
        char = ' '

    # Checking weather the word is guessed completely and printing 'won the game' and braking of while loop.
    if random_word == ''.join(guess_word[:word_length]):
        print('You have won the Game.')
        print('The word is', random_word)
        break

    # Displaying remaining attempts and guessing of character.
    print('\nAttempts remaining:', no_of_attempts)
    char = input('Guess the character: ')
    no_of_attempts -= 1

# If word is not guessed properly.
if random_word != ''.join(guess_word[:word_length]):
    print('Sorry! you have lost the game\nBetter luck next time!')
    print('The word is', random_word)
