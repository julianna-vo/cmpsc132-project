# Number Guessing Game 

import random

def number_guessing_game():
    target_number = random.randint(1,100) # Generate a random number from 1 to 100 and label it as the target number
    correct_guess = False # Create a correct_guess variable and set it to a bool value of False since user has not correctly guessed the number yet
    num_attempts = 0 # Set intialization variable to 0 to track number of attempts user makes to guess target number

    print("Hello and Welcome to the Number Guessing Game!")

    while not correct_guess:
        try:
            user_guess = int(input("Guess the number: ")) # Have user input their guess
            num_attempts += 1 # Increment num_attempts by 1 

        except ValueError:
            print("Your guess should be a valid digit!") # Ensure that user input only contains digits

            if user_guess > target_number: # Feedback given if user's guess is too high from target number
                print("Too High")

            elif user_guess < target_number: # Feedback given if user's guess is too low from target number
                print("Too Low")

            else: # Scenario if user correctly guesses the target number correctly
                print("Correct!")
                print(f"Congratulations! You guessed the correct number in {num_attempts} attempts!")
                correct_guess = True


"""
Extra implementations:
- Give hints for user after each incorrect guess
- Create certain difficulty modes
- Display a history summary at the end to display all of user's previous guesses
- More interactive comments

""" 