import random

player = input("ENTER NAME: ")
print("WELCOME", player, "FOR PARTICIPATING IN THIS ROCK PAPER SCISSORS GAME.\n" "WINNING RULES OF THE GAME ARE \n" "ROCK VS SCISSORS -> ROCK WINS \n" "PAPER VS ROCK -> PAPER WINS \n" "SCISSORS VS PAPER -> SCISSORS WINS \n")

while True:
    print("ENTER YOUR CHOICE\n 1 -> ROCK \n 2 -> PAPER \n 3 -> SCISSORS \n")
    choice = int(input("ENTER YOUR CHOICE: "))

    if choice < 1 or choice > 3:
        choice = int(input("ENTER A VALID CHOICE: "))

    if choice == 1:
        choice_name = 'ROCK'
    elif choice == 2:
        choice_name = 'PAPER'
    else:
        choice_name = 'SCISSORS'

    print("YOUR CHOICE IS", choice_name)
    print("NOW IT'S COMPUTER'S TURN...")

    comp_choice = random.randint(1, 3)
    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        comp_choice_name = 'ROCK'
    elif comp_choice == 2:
        comp_choice_name = 'PAPER'
    else:
        comp_choice_name = 'SCISSORS'

    print("COMPUTER'S CHOICE IS", comp_choice_name)
    print(choice_name, 'vs', comp_choice_name)

    if choice == comp_choice:
        print('IT IS A DRAW', end="")
        result = "DRAW"
    elif (choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 1):
        print('PAPER WINS =>', end="")
        result = 'PAPER'
    elif (choice == 1 and comp_choice == 3) or (choice == 3 and comp_choice == 1):
        print('ROCK WINS =>\n', end="")
        result = 'ROCK'
    else:
        print('SCISSORS WINS =>', end="")
        result = 'SCISSORS'

    if result == 'DRAW':
        print("<== IT IS A TIE ==>")
    elif result == choice_name:
        print("<== USER WINS ==>")
    else:
        print("<== COMPUTER WINS ==>")

    print("DO YOU WANT TO PLAY AGAIN? (Y/N)")
    ans = input()
    if ans == 'n' or ans == 'N':
        break

print("THANKS FOR PLAYING")