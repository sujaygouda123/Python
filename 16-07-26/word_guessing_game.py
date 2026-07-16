"""Word Guessing Game (Mini Hangman)."""

import random

WORDS = ("python", "machine", "learning", "bridge")
MAX_ATTEMPTS = 6


def get_display_word(word: str, guessed: set) -> str:
    return " ".join(ch if ch in guessed else "_" for ch in word)


def get_guess(guessed: set) -> str:
    """Prompt until the player enters a fresh, single letter."""
    while True:
        letter = input("Guess a letter: ").strip().lower()
        if len(letter) != 1 or not letter.isalpha():
            print("Please enter a single letter.")
            continue
        if letter in guessed:
            print(f"You already guessed '{letter}'.")
            continue
        return letter


def play() -> None:
    word = random.choice(WORDS)
    guessed = set()
    wrong_count = 0

    print("Word Guessing Game (Mini Hangman)")
    while wrong_count < MAX_ATTEMPTS:
        print(get_display_word(word, guessed))
        print(f"Wrong guesses: {wrong_count}/{MAX_ATTEMPTS}")

        letter = get_guess(guessed)
        guessed.add(letter)

        if letter in word:
            if all(ch in guessed for ch in word):
                print(get_display_word(word, guessed))
                print(f"You guessed it! The word was '{word}'.")
                return
        else:
            wrong_count += 1
            print(f"'{letter}' is not in the word.")

    print(f"Out of attempts! The word was '{word}'.")


def main() -> None:
    try:
        play()
    except (EOFError, KeyboardInterrupt):
        print("\nGame interrupted. Goodbye!")


if __name__ == "__main__":
    main()
