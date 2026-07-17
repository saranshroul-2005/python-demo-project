"""
Number Guessing Game
---------------------
A entertaining aware game where the player tries to guess a randomly
generated number within a limited number of attempts.

Author: SARANSH ROUL
"""
import random


class NumberGuessingGame:

    SPICE_LEVELS = {
        "1": {"label": "Spicy", "range": (1, 50), "attempts": 9},
        "2": {"label": "Medium Spicy", "range": (1, 100), "attempts": 7},
        "3": {"label": "Fire", "range": (1, 200), "attempts": 6},
    }

    def __init__(self, spice="2"):
        settings = self.SPICE_LEVELS.get(spice, self.SPICE_LEVELS["2"])

        self.low = settings["range"][0]
        self.high = settings["range"][1]
        self.max_attempts = settings["attempts"]

        self.target_number = random.randint(self.low, self.high)
        self.attempts_used = 0
        self.won = False

    def guess(self, number):
        self.attempts_used += 1

        if number == self.target_number:
            self.won = True
            return "correct"
        elif number < self.target_number:
            return "low"
        else:
            return "high"

    @property
    def attempts_remaining(self):
        return self.max_attempts - self.attempts_used

    @property
    def is_over(self):
        return self.won or self.attempts_remaining == 0


def get_valid_integer(prompt, low, high):

    while True:
        try:
            number = int(input(prompt))

            if low <= number <= high:
                return number

            print(f"Enter a number between {low} and {high}.")

        except ValueError:
            print("Please enter a valid whole number.")


def choose_spice():

    print("\nChoose Your Spice Level\n")

    for key, level in NumberGuessingGame.SPICE_LEVELS.items():
        low, high = level["range"]

        print(
            f"{key}. {level['label']} "
            f"(Range: {low}-{high}, Attempts: {level['attempts']})"
        )

    choice = input("\nEnter your choice (1/2/3): ").strip()

    if choice in NumberGuessingGame.SPICE_LEVELS:
        return choice

    print("Invalid choice. Medium Spicy selected by default.")
    return "2"


def play_round():

    spice = choose_spice()
    game = NumberGuessingGame(spice)

    print(f"\nThink a number between {game.low} and {game.high}.")
    print(f"You have {game.max_attempts} attempts.\n")

    while not game.is_over:

        guess = get_valid_integer(
            f"Attempt {game.attempts_used + 1}/{game.max_attempts}: ",
            game.low,
            game.high,
        )

        result = game.guess(guess)

        if result == "correct":
            print(f"\nGAME OVER! You guessed the number in {game.attempts_used} attempts.")
            return

        elif result == "low":
            print(f" higher! Attempts left: {game.attempts_remaining}")

        else:
            print(f" lower! Attempts left: {game.attempts_remaining}")

    print(f"\nGame Over! The correct number was {game.target_number}.")


def main():

    print("=" * 45)
    print("      NUMBER GUESSING GAME")
    print("=" * 45)

    while True:

        play_round()

        again = input("\nDo you want to play again? (once more/never again): ").strip().lower()

        if again != "once more":
            print("\nThanks for playing!")
            break


if __name__ == "__main__":
    main()