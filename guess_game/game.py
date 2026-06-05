import random

class NumberGuessingGame:
    """
    Core game logic for the Number Guessing Game.
    """
    def __init__(self, target_number=None, min_val=1, max_val=100, max_attempts=10):
        self.min_val = min_val
        self.max_val = max_val
        self.max_attempts = max_attempts
        # If no target number is provided, pick a random one
        self.target_number = target_number if target_number is not None else random.randint(min_val, max_val)
        self.attempts = 0
        self.game_over = False
        self.won = False

    def guess(self, number: int) -> str:
        """
        Make a guess. Returns a string code indicating the outcome:
        - 'correct': The guess is correct. The game ends in victory.
        - 'too_low': The guess is too low, and attempts remain.
        - 'too_high': The guess is too high, and attempts remain.
        - 'game_over_lost': The guess is wrong, and no attempts remain. The game ends in defeat.
        - 'already_over': The game has already ended.
        """
        if self.game_over:
            return "already_over"

        self.attempts += 1

        if number == self.target_number:
            self.game_over = True
            self.won = True
            return "correct"
        
        if self.attempts >= self.max_attempts:
            self.game_over = True
            self.won = False
            return "game_over_lost"

        if number < self.target_number:
            return "too_low"
        else:
            return "too_high"


def run_cli_game(game_instance=None, input_func=input, print_func=print):
    """
    CLI Runner for the Number Guessing Game.
    Accepts custom input/print functions for easy testing.
    """
    print_func("=== Welcome to the Number Guessing Game ===")
    
    if game_instance is None:
        game_instance = NumberGuessingGame()
        
    print_func(f"I'm thinking of a number between {game_instance.min_val} and {game_instance.max_val}.")
    print_func(f"You have {game_instance.max_attempts} attempts to guess it!")

    while not game_instance.game_over:
        remaining_attempts = game_instance.max_attempts - game_instance.attempts
        print_func(f"\nRemaining attempts: {remaining_attempts}")
        
        try:
            user_input = input_func("Enter your guess: ")
            guess_val = int(user_input)
        except ValueError:
            print_func("Error: Please enter a valid integer.")
            continue

        result = game_instance.guess(guess_val)
        
        if result == "correct":
            print_func(f"Congratulations! You guessed the number {game_instance.target_number} in {game_instance.attempts} attempts!")
        elif result == "too_low":
            print_func("Too low! Try a higher number.")
        elif result == "too_high":
            print_func("Too high! Try a lower number.")
        elif result == "game_over_lost":
            print_func(f"Game over! You've run out of attempts. The number was {game_instance.target_number}.")


if __name__ == "__main__":
    run_cli_game()
