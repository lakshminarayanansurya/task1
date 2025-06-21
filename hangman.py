import random

# List of 5 predefined words
words = ["apple", "banana", "cherry", "grape", "mango"]
word_to_guess = random.choice(words)

# Create a display version of the word with underscores
guessed_word = ["_"] * len(word_to_guess)
guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

print("Welcome to Hangman!")
print("Guess the word: " + " ".join(guessed_word))

while incorrect_guesses < max_incorrect and "_" in guessed_word:
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print("Good guess!")
        for i, letter in enumerate(word_to_guess):
            if letter == guess:
                guessed_word[i] = guess
    else:
        incorrect_guesses += 1
        print(f"Wrong guess! You have {max_incorrect - incorrect_guesses} guesses left.")

    print("Current word: " + " ".join(guessed_word))

# End of game
if "_" not in guessed_word:
    print("Congratulations! You guessed the word:", word_to_guess)
else:
    print("Game over! The word was:", word_to_guess)
