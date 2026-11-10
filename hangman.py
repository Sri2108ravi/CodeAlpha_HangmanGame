import random

# List of 5 predefined words
words = ["apple", "banana", "tiger", "python", "school"]

# Select a random word
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("===== WELCOME TO HANGMAN GAME =====")

while wrong_guesses < max_wrong_guesses:

    # Display the word with blanks
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Wrong guesses left:", max_wrong_guesses - wrong_guesses)

    # Check whether the player won
    if all(letter in guessed_letters for letter in word):
        print("\nCongratulations! You won!")
        break

    # Get input from player
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter!")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

else:
    print("\nGame Over!")
    print("The correct word was:", word)
