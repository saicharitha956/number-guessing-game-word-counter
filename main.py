
import random
import string
from collections import Counter


# Part 1: Number Guessing Game
def number_guessing_game():
    best_score = None

    while True:
        secret_number = random.randint(1, 100)
        attempts = 0
        score = 100
        max_attempts = 10

        print("\n=== Number Guessing Game ===")
        print("Guess a number between 1 and 100.")
        print("You have 10 attempts.")

        while attempts < max_attempts:
            try:
                guess = int(input("Enter your guess: "))
            except ValueError:
                print("Please enter a valid whole number.")
                continue

            if guess < 1 or guess > 100:
                print("Enter a number between 1 and 100.")
                continue

            attempts += 1

            if guess < secret_number:
                print("Too low!")
                score -= 10
            elif guess > secret_number:
                print("Too high!")
                score -= 10
            else:
                print("Correct! You guessed the number.")
                break

        else:
            print("Game over! The number was:", secret_number)

        final_score = max(score, 0)

        print("Attempts:", attempts)
        print("Final score:", final_score)

        if best_score is None or final_score > best_score:
            best_score = final_score

        print("Best score:", best_score)

        replay = input("Play again? (yes/no): ").strip().lower()

        if replay != "yes":
            break


# Part 2: Count Words in a Text File
def count_words(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            text = file.read().lower()

    except FileNotFoundError:
        print("File not found:", path)
        return None

    # Remove punctuation
    text = text.translate(
        str.maketrans("", "", string.punctuation)
    )

    # Split text into words
    words = text.split()

    # Count word frequencies
    return Counter(words)


def word_counter():
    print("\n=== Word Counter ===")

    filename = input(
        "Enter text filename (e.g., sample.txt): "
    )

    counts = count_words(filename)

    if counts is not None:
        print("\nTotal words:", sum(counts.values()))
        print("Unique words:", len(counts))

        print("\nTop 10 Most Frequent Words")
        print("-" * 25)

        for word, frequency in counts.most_common(10):
            print(f"{word:<15}{frequency:>5}")


# Part 3: Main Menu
def main():
    while True:
        print("\n=== Python Tools ===")
        print("1. Number Guessing Game")
        print("2. Word Counter")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            number_guessing_game()
        elif choice == "2":
            word_counter()
        elif choice == "3":
            print("Thank you for using Python Tools!")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")


# Start the program
if __name__ == "__main__":
    main()
