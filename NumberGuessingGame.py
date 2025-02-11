# Description: A simple number guessing game where the user has to guess a number between 1 and 100. The program will tell the user if their guess is too high or too low, and will keep track of the number of attempts it took to guess the correct number. The user can choose to play again or exit the game.

import random
def number_guessing_game():
    while True:
        target = random.randint(1, 100)
        attempts = 0
        print("Guess the number (between 1 and 100):")
        
        while True:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < target:
                print("Too low!")
            elif guess > target:
                print("Too high!")
            else:
                print(f"Correct! You guessed it in {attempts} attempts.")
                break
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

# Example usage
number_guessing_game()
