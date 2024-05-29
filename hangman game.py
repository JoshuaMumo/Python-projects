#hangman game
import random

name = input("Enter name: ")
print("Guess any alphabet", name)

words = ["chair", "table", "laptop", "desktop", "mouse"]
x = random.choice(words)
guesses = ''
turns = 12

while turns > 0:
    failed = 0
    for char in x:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1
    if failed == 0:
        print("\nCongratulations. The word is", x)
        break

    print()
    guess = input("Input character: ")
    guesses += guess

    if guess not in x:
        turns -= 1
        print("Wrong")
        print("You have", turns, "more guesses")

    if turns == 0:
        print("You lose")
