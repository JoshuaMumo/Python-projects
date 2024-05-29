#word guessing game
import random
from collections import Counter

someWords = ['chair', 'table', 'laptop', 'desktop', 'mouse']
playing = True

while playing:
    letterGuessed = ''
    word = random.choice(someWords)
    chances = len(word) + 2
    correct = 0

    print("HINT! The word is a name of an office equipment.")

    while chances > 0:
        try:
            guess = str(input("Enter letter to guess: "))
            if not guess.isalpha():
                raise ValueError("Enter only a letter")
        except ValueError as e:
            print(e)
            continue

        if guess in word:
            letterGuessed += guess
            for char in word:
                if char in letterGuessed:
                    print(char, end=" ")
                    correct += 1
                else:
                    print("_", end=" ")
            print()
            if Counter(letterGuessed) == Counter(word):
                print("Congratulations! You won")
                break
        else:
            chances -= 1
            print("Wrong guess. You have", chances, "chances left.")
            if chances == 0:
                print("You lost! Try again")
                print("The word was", word)
                break

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != 'y':
        break