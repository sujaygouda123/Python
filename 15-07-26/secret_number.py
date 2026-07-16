"""A simple number-guessing game."""

import random

MIN_NUMBER = 1
MAX_NUMBER = 100
MAX_ATTEMPTS = 7


def get_guess(min_number: int, max_number: int) -> int:
    """Prompt the user until they enter a valid integer in range."""
    while True:
        raw = input(f"Take a guess ({min_number}-{max_number}): ").strip()
        try:
            guess = int(raw)
        except ValueError:
            print("Please enter a whole number.")
            continue
        if not min_number <= guess <= max_number:
            print(f"Please enter a number between {min_number} and {max_number}.")
            continue
        return guess


def play(min_number: int = MIN_NUMBER, max_number: int = MAX_NUMBER, max_attempts: int = MAX_ATTEMPTS) -> None:
    """Run one round of the secret number game."""
    print("Welcome to the Secret Number Game!")
    print(f"I'm thinking of a number between {min_number} and {max_number}.")

    secret_number = random.randint(min_number, max_number)

    for attempt in range(1, max_attempts + 1):
        guess = get_guess(min_number, max_number)

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Congratulations! You've guessed the secret number {secret_number} in {attempt} attempt(s).")
            return

    print(f"Sorry, you've used all {max_attempts} attempts. The secret number was {secret_number}.")


if __name__ == "__main__":
    play()
