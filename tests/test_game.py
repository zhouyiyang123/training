import unittest
from guess_game.game import NumberGuessingGame, run_cli_game

class TestNumberGuessingGame(unittest.TestCase):
    def test_init_default(self):
        """Test initialization with default parameters."""
        game = NumberGuessingGame()
        self.assertEqual(game.min_val, 1)
        self.assertEqual(game.max_val, 100)
        self.assertEqual(game.max_attempts, 10)
        self.assertTrue(game.min_val <= game.target_number <= game.max_val)
        self.assertEqual(game.attempts, 0)
        self.assertFalse(game.game_over)
        self.assertFalse(game.won)

    def test_init_custom(self):
        """Test initialization with custom parameters."""
        game = NumberGuessingGame(target_number=42, min_val=10, max_val=50, max_attempts=5)
        self.assertEqual(game.min_val, 10)
        self.assertEqual(game.max_val, 50)
        self.assertEqual(game.max_attempts, 5)
        self.assertEqual(game.target_number, 42)

    def test_guess_too_low(self):
        """Test feedback for a guess that is too low."""
        game = NumberGuessingGame(target_number=50)
        result = game.guess(30)
        self.assertEqual(result, "too_low")
        self.assertEqual(game.attempts, 1)
        self.assertFalse(game.game_over)
        self.assertFalse(game.won)

    def test_guess_too_high(self):
        """Test feedback for a guess that is too high."""
        game = NumberGuessingGame(target_number=50)
        result = game.guess(70)
        self.assertEqual(result, "too_high")
        self.assertEqual(game.attempts, 1)
        self.assertFalse(game.game_over)
        self.assertFalse(game.won)

    def test_guess_correct(self):
        """Test feedback for a correct guess."""
        game = NumberGuessingGame(target_number=50)
        result = game.guess(50)
        self.assertEqual(result, "correct")
        self.assertEqual(game.attempts, 1)
        self.assertTrue(game.game_over)
        self.assertTrue(game.won)

    def test_game_over_lost(self):
        """Test running out of attempts."""
        game = NumberGuessingGame(target_number=50, max_attempts=3)
        # Attempt 1
        self.assertEqual(game.guess(10), "too_low")
        # Attempt 2
        self.assertEqual(game.guess(20), "too_low")
        # Attempt 3 - last attempt, wrong guess
        self.assertEqual(game.guess(30), "game_over_lost")
        self.assertTrue(game.game_over)
        self.assertFalse(game.won)

    def test_guess_already_over(self):
        """Test that guessing after game is over returns already_over."""
        game = NumberGuessingGame(target_number=50)
        self.assertEqual(game.guess(50), "correct")
        self.assertEqual(game.guess(30), "already_over")


class TestCLIRunner(unittest.TestCase):
    def test_cli_game_won(self):
        """Test CLI workflow when the player wins."""
        # Inputs to provide: guess 50 (correct)
        inputs = ["50"]
        printed_messages = []

        def mock_input(prompt):
            return inputs.pop(0)

        def mock_print(message):
            printed_messages.append(message)

        game = NumberGuessingGame(target_number=50)
        run_cli_game(game, input_func=mock_input, print_func=mock_print)

        # Check if the winning message is printed
        self.assertTrue(any("Congratulations" in msg for msg in printed_messages))
        self.assertTrue(game.game_over)
        self.assertTrue(game.won)

    def test_cli_game_lost(self):
        """Test CLI workflow when the player loses."""
        # Custom 2 attempts max. Inputs: 10, 20 (both wrong)
        inputs = ["10", "20"]
        printed_messages = []

        def mock_input(prompt):
            return inputs.pop(0)

        def mock_print(message):
            printed_messages.append(message)

        game = NumberGuessingGame(target_number=50, max_attempts=2)
        run_cli_game(game, input_func=mock_input, print_func=mock_print)

        self.assertTrue(any("Game over" in msg for msg in printed_messages))
        self.assertTrue(game.game_over)
        self.assertFalse(game.won)

    def test_cli_invalid_input(self):
        """Test CLI recovery from invalid non-integer inputs."""
        # First input: invalid "abc", second input: 50 (correct)
        inputs = ["abc", "50"]
        printed_messages = []

        def mock_input(prompt):
            return inputs.pop(0)

        def mock_print(message):
            printed_messages.append(message)

        game = NumberGuessingGame(target_number=50)
        run_cli_game(game, input_func=mock_input, print_func=mock_print)

        self.assertTrue(any("Please enter a valid integer" in msg for msg in printed_messages))
        self.assertTrue(game.game_over)
        self.assertTrue(game.won)


if __name__ == "__main__":
    unittest.main()
#niude