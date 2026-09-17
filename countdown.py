# Part A — Countdown

def main():
    # Ask the user for a starting number
    user_input = input("Enter a number to start the countdown from: ")
    count = int(user_input)

    # While loop to count down from the starting number to 1
    while count > 0:
        print(count)
        count -= 1  # Decrement the loop variable so it doesn't loop forever

    # Print blast off message after the loop finishes
    print("Blast off!")

if __name__ == "__main__":
    main()