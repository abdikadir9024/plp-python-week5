# Part B — Guessing Game

def main():
    secret_number = 12  # Secret number between 1 and 20
    attempts = 0
    guessed_correctly = False

    print("Welcome to the Guessing Game! Guess a number between 1 and 20.")

    # Loop until the user guesses the correct number
    while not guessed_correctly:
        guess = int(input("Enter your guess: "))
        attempts += 1  # Track the number of tries

        if guess > secret_number:
            print("Too high!")
        elif guess < secret_number:
            print("Too low!")
        else:
            print(f"Congratulations! You got it in {attempts} tries!")
            guessed_correctly = True  # Ends the loop

if __name__ == "__main__":
    main()