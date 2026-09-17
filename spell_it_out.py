 # Part C — Spell It Out

def main():
    word = input("Enter a word: ")

    # First loop: Print each letter on its own line
    print("\nLetters in your word:")
    for letter in word:
        print(letter)

    # Second loop: Print numbered letters (1-indexed)
    print("\nNumbered letters:")
    for index, letter in enumerate(word, start=1):
        print(f"{index}. {letter}")

    # Display total character count
    print(f"\nYour word has {len(word)} letters.")

if __name__ == "__main__":
    main()