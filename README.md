# Hangman-Game
Hangman Game using python

The Hangman game(Guess the word) is implemented using python. The user needs to enter the number of chances he need to guess the word and select the size of the word. After entering the both inputs user can start playing the game. If the word is guessed properly with in the number of choices he/she won the game or else not.

# Algorithm
1. Getting input for number of choices.
2. Getting input for length of the word.
3. Open the file containing the words in read mode.
4. Reading all the words in the file and filter the words having same length given by the user.
5. Picking up a random word from the filtered list of words.
6. Starting with guessing of charecters/alphabets.
7. Creating a string(guess_word) with hyphens/stars.
8. Printing the string.
9. loop: 
9. 1. checking weather the input charecter is present in string or not.
9. 2. if present print the charecter in the same position as it in the random word selected and replace guess_word with the charecter at same position.
9. 3. if guess_word is equal to random_word print "won the game"&"random_word" break the loop and goto step 10.
9. 4. getting the charecter input from the user.
10. if random word is not equal to guess_word print "You have lost the game"&"random_word".
