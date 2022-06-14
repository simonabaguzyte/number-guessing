from random import randint


print("\n\n*** WELCOME TO THE NUMBER GUESSING PROGRAM! ***")
print("\nThe program automaticly selects one number from 1 to 100 in integers scale.\
\nYour task is to guess that number. Do not worry, you are going to get some hints if needed.\
\nGood luck!\n")


print("\nLet the guessing begin!")

shouldContinue = True
while shouldContinue:

    randomNumber = randint(1, 100)
    print("*Psst, the random number is %s.*" % (randomNumber))

    shouldContinue2 = True
    while shouldContinue2:

        guess = int(input("\nEnter your guess (1-100): "))

        if guess < 1 or guess > 100:
            print("Your input is not in the scale from 1 to 100.\n")
            print("Please, check your input and try again.")

        elif guess == randomNumber:
            print("BRAVO!!! You have guessed it! The number was %s." % randomNumber)
            choice = input("\n\nWould you like to play again (Y/N)?: ")
            print("\n-------------------------------------------------")
            if choice.startswith('y' or 'Y'):
                shouldContinue2 = False
                shouldContinue = False
                shouldContinue = True
            elif choice.startswith('n' or 'N'):
                shouldContinue = False
                shouldContinue2 = False
                print("\nThanks for using my number guessing program.")
                print("I hope to see you next time!")
        else:
            if guess > randomNumber:
                print("Try smaller number.")
            elif guess < randomNumber:
                print("Try bigger number.")