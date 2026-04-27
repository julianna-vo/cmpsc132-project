# Number Guessing Game 

import random

def number_guessing_game():

    # Introduction statement
    print("\n Hello and Welcome to the Number Guessing Game!")

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
            
        if max_attempts != float('inf'): # Scenario if max_attempts aren't unlimited, keep track of remaining attempts for user
                remaining_attempts = max_attempts - num_attempts
                print(f"You have {remaining_attempts} tries left to guess!")

        try:
            user_guess = int(input("Guess the number: ")) # Have user input their guess
            num_attempts += 1 # Increment num_attempts by 1 

        except ValueError:
            print("Your guess should be a valid digit!") # Ensure that user input only contains digits

        if user_guess > target_number: # Feedback given if user's guess is too high from target number
            print("Too High")
                    

        elif user_guess < target_number: # Feedback given if user's guess is too low from target number
            print("Too Low")

        if (user_guess > target_number) or (user_guess < target_number): # Give hints to whether target number is even or odd only if hints_on (EASY OR MEDIUM MODE)
            if hints_on:
                if target_number % 2 == 0:
                    print("HINT: The target number is even...")

                if target_number % 2 != 0:
                            print("HINT: The target number is odd...")

        else: # Scenario if user correctly guesses the target number correctly
            print("\nCorrect!")
            print(f"Congratulations! You guessed the correct number in {num_attempts} attempts!")
            correct_guess = True
            guess_history.append((num_attempts, user_guess)) # Keep track of user's guess history

        if not correct_guess and (max_attempts - num_attempts) == 0:
            print(f"You're out of attempts! Game over!")
            break

        if not correct_guess:
            guess_history.append((num_attempts, user_guess))
                
    # Display a history log of user's attempts
    print("Let's look at a summary of all of your attempts!")
    for attempt_num, guess in guess_history:
        print(f"Attempt {attempt_num}: {guess}")


number_guessing_game()
                
            
"""
Extra implementations:
- Give hints for user after each incorrect guess (states if target number is even or odd) if user selects EASY or MEDIUM MODE
- Create certain difficulty modes (EASY, MEDIUM, HARD)
- Display a history summary at the end to display all of user's previous guesses
- Tell user how many attempts they have left after each guess
""" 