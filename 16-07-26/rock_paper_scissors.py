"""Rock, Paper, Scissors — player vs. computer."""

import random

CHOICES = ("rock", "paper", "scissors")
BEATS = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
MENU = {"1": "rock", "2": "paper", "3": "scissors"}


def get_player_choice() -> str:
    """Prompt until the player enters a valid menu number."""
    print("1) Rock  2) Paper  3) Scissors")
    while True:
        choice = input("Enter your choice (1-3): ").strip()
        if choice in MENU:
            return MENU[choice]
        print(f"Invalid choice '{choice}'. Please enter 1, 2, or 3.")


def decide_winner(player: str, computer: str) -> str:
    """Return 'player', 'computer', or 'tie'."""
    if player == computer:
        return "tie"
    if BEATS[player] == computer:
        return "player"
    return "computer"


def play_round() -> None:
    player = get_player_choice()
    computer = random.choice(CHOICES)
    print(f"Computer chose {computer}.")

    result = decide_winner(player, computer)
    if result == "tie":
        print("It's a tie!")
    elif result == "player":
        print("You win!")
    else:
        print("Computer wins!")


def main() -> None:
    print("Rock, Paper, Scissors!")
    try:
        while True:
            play_round()
            again = input("Play again? (y/n): ").strip().lower()
            if again != "y":
                print("Thanks for playing!")
                break
    except (EOFError, KeyboardInterrupt):
        print("\nGame interrupted. Goodbye!")


if __name__ == "__main__":
    main()
