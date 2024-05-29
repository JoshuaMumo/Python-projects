#21 number game
import random

def player_turn(current_total):
    print("Current total:", current_total)
    while True:
        try:
            choice = int(input("Enter 1 to 3: "))
            if choice < 1 or choice > 3:
                print("Invalid input. Enter a number between 1 and 3.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter a number between 1 and 3.")
    return choice

def computer_turn(current_total):
    if current_total % 4 == 0:
        return random.randint(1, 3)
    else:
        return 4 - (current_total % 4)

def main():
    total = 0
    print("Welcome to the 21 Number Game!")
    print("You and the computer will take turns adding 1, 2, or 3 to a running total.")
    print("The player who reaches 21 exactly wins!")
    while total < 21:
        player_choice = player_turn(total)
        total += player_choice
        if total >= 21:
            print("You win!")
            break
        print("Total after your turn:", total)
        computer_choice = computer_turn(total)
        print("Computer chooses:", computer_choice)
        total += computer_choice
        if total >= 21:
            print("Computer wins!")
            break
        print("Total after computer's turn:", total)

if __name__ == "__main__":
    main()