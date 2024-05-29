#mastermind game challenge
import random

num = random.randrange(1000, 10000)
n = int(input("Welcome to the mastermind game challenge. \nGuess the number: "))

if n == num:
    print("Congratulations! You guessed correctly in the first try")
else:
    ctr = 0
    while n != num:
        ctr += 1
        count = 0
        n = str(n)
        num = str(num)
        correct = ['_'] * 4
        for i in range(0, 4):
            if n[i] == num[i]:
                count += 1
                correct[i] = n[i]
            else:
                continue
        print("Not quite the number but you still got", count, "digit(s) correctly")
        print('\n')
        print('\n')
        n = int(input("Enter your next choice of numbers: "))
        if count == 0:
            print("None of the numbers you input match")
            n = int(input("Enter your next choice of numbers: "))

    if n == num:
        ctr += 1
        print("You have become a mastermind in", ctr, "trials")