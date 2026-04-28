# Number Guessing Game 

import random

def number_guessing_game():

    # Introduction statement
    print("\n" + "="*50) 
    print("\n Hello and Welcome to the Number Guessing Game!")
    print("\n" + "="*50)

    # Player gets to choose the difficulty mode
    print("\n Select a difficulty mode!")
    print(" 1. Easy Mode: Target number rangers from 1-50, unlimited guesses, hint given after each guess")
    print(" 2. Medium Mode: Target number rangers from 1-100, 20 guesses, hint given after each guess")
    print(" 3. Difficult Mode: Target number rangers from 1-200, 10 guesses, no hints given")

    while True: 
        difficulty = input ("\nEnter 1, 2, or 3: ").strip()

        if difficulty == "1": 
            low, high, max_attempts, hints_on = 1,50, float('inf'), True
            print("You're on Easy Mode! Take it easy!")
            break

        elif difficulty == "2":
            low, high, max_attempts, hints_on = 1,100, 20, True
            print("You're on Medium Mode! A little more challenging!")
            break

        elif difficulty == "3":
            low, high, max_attempts, hints_on = 1,200, 10, False
            print("You're on Hard Mode! Game on!")
            break
        
        else:
            print("Please enter 1, 2, or 3!")

    target_number = random.randint(low, high) # Generate a random number from 1 to 100 and label it as the target number
    correct_guess = False # Create a correct_guess variable and set it to a bool value of False since user has not correctly guessed the number yet
    num_attempts = 0 # Set intialization variable to 0 to track number of attempts user makes to guess target number
    guess_history = []

    print(f"\nGuess a number between {low} and {high}!")

    while not correct_guess:

        try:
            user_guess = int(input("Guess the number: ")) # Have user input their guess
            num_attempts += 1 # Increment num_attempts by 1 
            guess_history.append((num_attempts, user_guess))

        except ValueError:
            print("Your guess should be a valid digit!") # Ensure that user input only contains digits
            continue 

        # Check the Guess
        # SCENARIO 1: guess matches target 
        if user_guess == target_number: # Feedback given if user's guess is too high from target number
            print("\nCorrect!")
            print(f"Congratulations! You guessed the correct number in {num_attempts} attempts!")
            correct_guess = True

        else:
            # SCENARIO 2: guess is lower than target
            if user_guess < target_number: # Feedback given if user's guess is too low from target number
                print("\n*** Too Low ***")

            # SCENARIO 3: guess is higher than target
            else:
                print("\n*** Too High ***")

            if hints_on: # Only for EASY and MEDIUM mode
                print("="*30)

                if target_number % 2 == 0: # Case if num is even
                    print("HINT: The target number is even...")

                else: # Case if num is odd
                    print("HINT: The target number is odd...")

                print("="*30)
            
            if max_attempts != float('inf'): # Scenario if max_attempts aren't unlimited, keep track of remaining attempts for user (MEDIUM and HARD MODE)
                remaining_attempts = int(max_attempts - num_attempts)

                if remaining_attempts > 0:
                    print(f"*** You have {remaining_attempts} tries left to guess! ***")

                else:
                    print(f"No more attempts left! Game over!\nThe correct number was {target_number}!")
                    break

    # Display a history log of user's attempts
    print("Let's look at a summary of all of your attempts!")
    for attempt_num, guess in guess_history:
        print(f"Attempt {attempt_num}: {guess}")
           
"""
Extra implementations:
- Give hints for user after each incorrect guess (states if target number is even or odd) if user selects EASY or MEDIUM MODE
- Create certain difficulty modes (EASY, MEDIUM, HARD)
- Display a history summary at the end to display all of user's previous guesses
- Tell user how many attempts they have left after each guess
- Implement a "play again" to reset the game again if the user wishes to 

""" 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def main():

    # Implement a "Play again" feature
    while True:
        number_guessing_game()

        play_again_choice = input("\nWant to play again? YES or NO: ").strip().lower()

        if play_again_choice != 'yes':
            print("Thanks for playing! See you next time!")
            break

if __name__ == "__main__":
    main()
