"""
Number Guessing Game
---------------------
A simple CLI game where the player tries to guess a randomly
generated number within a limited number of attempts.

Author: Your Name
"""

import random


class NumberGuessingGame:
    """Encapsulates the state and logic of a single game session."""

    DIFFICULTY_LEVELS = {
        "1": {"label": "Easy",   "range": (1, 50),  "attempts": 10},
        "2": {"label": "Medium", "range": (1, 100), "attempts": 7},
        "3": {"label": "Hard",   "range": (1, 200), "attempts": 5},
    }

    def __init__(self, difficulty: str = "2"):
        settings = self.DIFFICULTY_LEVELS.get(difficulty, self.DIFFICULTY_LEVELS["2"])
        self.low, self.high = settings["range"]
        self.max_attempts = settings["attempts"]
        self.attempts_used = 0
        self.target_number = random.randint(self.low, self.high)
        self.won = False

    def guess(self, value: int) -> str:
        """Process a single guess and return feedback as a string."""
        self.attempts_used += 1

        if value == self.target_number:
            self.won = True
            return "correct"
        elif value < self.target_number:
            return "low"
        else:
            return "high"

    @property
    def attempts_remaining(self) -> int:
        return self.max_attempts - self.attempts_used

    @property
    def is_over(self) -> bool:
        return self.won or self.attempts_remaining <= 0


def get_valid_integer(prompt: str, low: int, high: int) -> int:
    """Keep asking the user until a valid integer within range is entered."""
    while True:
        raw_input_value = input(prompt).strip()
        try:
            value = int(raw_input_value)
        except ValueError:
            print("❌ Please enter a whole number.")
            continue

        if value < low or value > high:
            print(f"❌ Please enter a number between {low} and {high}.")
            continue

        return value


def choose_difficulty() -> str:
    print("\nSelect difficulty:")
    for key, settings in NumberGuessingGame.DIFFICULTY_LEVELS.items():
        low, high = settings["range"]
        print(f"  {key}. {settings['label']} "
              f"(range {low}-{high}, {settings['attempts']} attempts)")

    choice = input("Enter choice (1/2/3), default is Medium: ").strip()
    return choice if choice in NumberGuessingGame.DIFFICULTY_LEVELS else "2"


def play_round():
    difficulty = choose_difficulty()
    game = NumberGuessingGame(difficulty)

    print(f"\nI'm thinking of a number between {game.low} and {game.high}.")
    print(f"You have {game.max_attempts} attempts. Good luck!\n")

    while not game.is_over:
        prompt = f"Attempt {game.attempts_used + 1}/{game.max_attempts} - Your guess: "
        guess_value = get_valid_integer(prompt, game.low, game.high)
        result = game.guess(guess_value)

        if result == "correct":
            print(f"🎉 Correct! You guessed it in {game.attempts_used} attempts.")
        elif result == "low":
            print(f"📈 Too low. {game.attempts_remaining} attempts left.")
        elif result == "high":
            print(f"📉 Too high. {game.attempts_remaining} attempts left.")

    if not game.won:
        print(f"\n💥 Out of attempts! The number was {game.target_number}.")


def main():
    print("=" * 40)
    print("   🎯 WELCOME TO THE NUMBER GUESSING GAME")
    print("=" * 40)

    while True:
        play_round()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing! 👋")
            break


if __name__ == "__main__":
    main()
