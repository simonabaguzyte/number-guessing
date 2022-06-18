from random import randint

MIN_VALUE = 1
MAX_VALUE = 100

def print_introduction():
    print("\n\n***WELCOME TO THE NUMBER GUESSING PROGRAM!***")
    print(f"\nThe program automatically selects one integer from {MIN_VALUE} to {MAX_VALUE}.")
    print("Your task is to guess that number. Do not worry, you are going to get some hints.")
    print("\nGood luck!")
    print("\nLet the guessing begin!")

def get_user_guess():
    while True:
        try:
            guess = int(input(f"\nEnter your guess ({MIN_VALUE}-{MAX_VALUE}): "))

            guess_is_inside_boundaries =  guess >= MIN_VALUE and guess <= MAX_VALUE
            if guess_is_inside_boundaries:
                break

            print(f"Your input is not on a scale of {MIN_VALUE} to {MAX_VALUE}. Try again:")
            continue
        except ValueError:
            print("You have entered a non-integer value. Try again:")
            continue

    return guess

def congratulate_winner(number_to_guess):
    print(f"BRAVO!!! You have guessed it! The number was {number_to_guess}.")

def play_game(number_to_guess):
    while True:
        guess = get_user_guess()
        if guess == number_to_guess:
            congratulate_winner(number_to_guess)
            break
        elif guess > number_to_guess:
            print("Try smaller number.")
        elif guess < number_to_guess:
            print("Try bigger number.")

def decide_if_play_again():   
    while True:
        choice = input("\n\nWould you like to play again (Y/N)?: ").lower()
        if choice == 'y' or choice == 'yes':
            print("\n-------------------------------------------------")
            return True
        elif choice == 'n' or choice == 'no':
            print("\nThanks for using my number guessing program.")
            print("I hope to see you next time!")
            return False
        else:
            print("There was no such choice. Try again:")

if __name__ == "__main__":
    print_introduction()

    should_continue = True
    while should_continue:
        random_number = randint(MIN_VALUE, MAX_VALUE)
        print(random_number)
        play_game(random_number)

        should_continue = decide_if_play_again()
