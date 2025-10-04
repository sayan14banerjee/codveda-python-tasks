import random

def guess_number():
    # Game introduction and difficulty selection
    print("Welcome to the Number Guessing Game!")
    print("Choose difficulty level:")
    print("1. Easy (10 attempts)")
    print("2. Medium (7 attempts)")
    print("3. Hard (5 attempts)")

    # Set attempts based on difficulty
    while True:
        difficulty = input("Enter 1, 2, or 3: ")
        if difficulty == '1':
            max_attempts = 10
            break
        elif difficulty == '2':
            max_attempts = 7
            break
        elif difficulty == '3':
            max_attempts = 5
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
    
    # Initialize game variables
    number_to_guess = random.randint(1,100)
    attempts = 0
    print("I have selected a number between 1 and 100. Can you guess it?")

    # Main game loop
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts+1}/{max_attempts} - Enter your guess: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        attempts += 1
        # Check the guess
        if guess == number_to_guess:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif guess < number_to_guess:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
    # Game over message
    else:
        print(f"Sorry! You've used all {max_attempts} attempts. The number was {number_to_guess}.")
    
    # Prompt for replay
    replay = input("Do you want to play again? (yes/no): ").strip().lower()
    if replay == 'yes':
        guess_number()
    else:
        print("Thank you for playing! Goodbye.")
    
    
if __name__ == "__main__":
    guess_number()    


