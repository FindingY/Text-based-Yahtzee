"""Main Yahtzee game controller."""

from die import Die
from scorecard import ScoreCard


class YahtzeeGame:
    """Control the flow of a single-player text-based Yahtzee game."""

    def __init__(self):
        # TODO: Create a list containing five Die objects.
        self.dice = []

        # The game has one ScoreCard.
        self.scorecard = ScoreCard()

    def roll_all_dice(self):
        """Roll all five dice."""
        # TODO: Roll every Die object in self.dice.
        pass

    def display_dice(self):
        """Display the five dice with positions numbered 1 through 5."""
        # TODO: Display output similar to:
        #
        # 1: [4]
        # 2: [1]
        # 3: [6]
        # 4: [4]
        # 5: [2]
        pass

    def get_dice_to_keep(self):
        """Ask the player which dice to keep and return their positions."""
        # TODO:
        # - Ask for input such as: 1 3 5
        # - Pressing Enter should return []
        # - Convert entries to integers
        # - Accept only values 1 through 5
        # - Use exception handling so bad input does not crash the program
        while True:
            try:
                text = input(
                    "Enter dice to KEEP separated by spaces "
                    "(or press Enter to keep none): "
                )

                # TODO: Process and validate text.

                pass

            except ValueError:
                print("Please enter only die numbers from 1 through 5.")

    def reroll_dice(self, keep):
        """Reroll every die whose displayed position is not in keep."""
        # TODO: Remember that list indexes begin at 0,
        # but the displayed die positions begin at 1.
        pass

    def get_dice_values(self):
        """Return the current five die values as a list of integers."""
        values = []

        # TODO: Call get_value() on each Die object.

        return values

    def choose_category(self):
        """Ask the player to choose one available scoring category."""
        # TODO:
        # 1. Get available categories from self.scorecard.
        # 2. Display them with numbers.
        # 3. Ask the player to choose a number.
        # 4. Validate the input.
        # 5. Return the selected category name.
        pass

    def play_turn(self):
        """Play one complete Yahtzee turn."""
        # TODO:
        # 1. Roll all dice.
        # 2. Allow up to three total rolls.
        # 3. Between rolls, ask which dice to keep.
        # 4. After the final roll, get the die values.
        # 5. Ask for a scoring category.
        # 6. Record the score.
        pass

    def get_scorecard_filename(self):
        """Ask for a filename and make sure it ends in .txt."""
        # TODO: Ask the player for a filename.
        # If it does not end with ".txt", add the extension.
        pass

    def play(self):
        """Play a complete 13-turn Yahtzee game."""
        print("=" * 30)
        print("YAHTZEE")
        print("=" * 30)

        # TODO:
        # Play 13 turns.
        #
        # Each turn should:
        # - display the turn number
        # - display the scorecard
        # - call play_turn()
        #
        # After the final turn:
        # - display GAME OVER
        # - display the completed scorecard
        # - display the total score
        # - ask for a filename
        # - save the scorecard to that file
        pass
