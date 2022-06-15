from random import randint


MIN_VALUE = 1
MAX_VALUE = 100

print("\n\n*** WELCOME TO THE NUMBER GUESSING PROGRAM! ***")
print(f"\nThe program automaticly selects one number from {MIN_VALUE} to {MAX_VALUE} in integers scale.\
\nYour task is to guess that number. Do not worry, you are going to get some hints if needed.\
\nGood luck!\n")


print("\nLet the guessing begin!")

shouldContinue = True
while shouldContinue:

    randomNumber = randint(MIN_VALUE, MAX_VALUE)

    shouldContinue2 = True
    while shouldContinue2:

        # neveikia, kai rasai raide
        guess = int(input(f"\nEnter your guess ({MIN_VALUE}-{MAX_VALUE}): "))

        if guess < MIN_VALUE or guess > MAX_VALUE:
            print(f"Your input is not in the scale from {MIN_VALUE} to {MAX_VALUE}.\n")
            print("Please, check your input and try again.")

        elif guess == randomNumber:
            print(f"BRAVO!!! You have guessed it! The number was {randomNumber}.")
            choice = input("\n\nWould you like to play again (Y/N)?: ").lower()
            print("\n-------------------------------------------------")
            if choice == 'y' or choice == 'yes':
                #break
                shouldContinue2 = False
            elif choice == 'n' or choice == 'no':
                shouldContinue = False
                shouldContinue2 = False
                print("\nThanks for using my number guessing program.")
                print("I hope to see you next time!")
        else:
            if guess > randomNumber:
                print("Try smaller number.")
            elif guess < randomNumber:
                print("Try bigger number.")