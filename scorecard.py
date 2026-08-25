"""ScoreCard class for the Yahtzee project."""


class ScoreCard:
    """Store and calculate scores for one Yahtzee game."""

    def __init__(self):
        # None means the category has not yet been used.
        self.scores = {
            "Ones": None,
            "Twos": None,
            "Threes": None,
            "Fours": None,
            "Fives": None,
            "Sixes": None,
            "Three of a Kind": None,
            "Four of a Kind": None,
            "Full House": None,
            "Small Straight": None,
            "Large Straight": None,
            "Yahtzee": None,
            "Chance": None,
        }

    def display(self):
        """Display the current scorecard."""
        # TODO: Print each category and its score.
        # Display unused categories as --.
        pass

    def get_counts(self, values):
        """Return a dictionary counting how often each die value occurs."""
        # Example:
        # [4, 4, 2, 4, 6] -> {4: 3, 2: 1, 6: 1}
        counts = {}

        # TODO: Build and return the counts dictionary.

        return counts

    def three_of_a_kind(self, values):
        """Return the Three of a Kind score."""
        # TODO: If at least three dice match, return the sum of all dice.
        # Otherwise return 0.
        pass

    def four_of_a_kind(self, values):
        """Return the Four of a Kind score."""
        # TODO: If at least four dice match, return the sum of all dice.
        # Otherwise return 0.
        pass

    def full_house(self, values):
        """Return the Full House score."""
        # TODO: A full house contains one pair and one group of three.
        # Return 25 for a full house and 0 otherwise.
        pass

    def small_straight(self, values):
        """Return the Small Straight score."""
        # TODO: Check for one of:
        # 1,2,3,4
        # 2,3,4,5
        # 3,4,5,6
        # Return 30 if found and 0 otherwise.
        pass

    def large_straight(self, values):
        """Return the Large Straight score."""
        # TODO: Check for:
        # 1,2,3,4,5
        # or
        # 2,3,4,5,6
        # Return 40 if found and 0 otherwise.
        pass

    def yahtzee(self, values):
        """Return the Yahtzee score."""
        # TODO: Return 50 if all five values match.
        # Otherwise return 0.
        pass

    def calculate_score(self, category, values):
        """Calculate and return a score for the selected category."""
        # TODO: Implement all 13 scoring categories.
        #
        # Suggested structure:
        #
        # if category == "Ones":
        #     ...
        # elif category == "Twos":
        #     ...
        #
        # Use the helper methods above for the more complicated categories.
        pass

    def record_score(self, category, values):
        """Record the score for one category."""
        # TODO:
        # 1. Make sure the category has not already been used.
        # 2. Calculate the score.
        # 3. Store the score.
        # 4. Return True if successful and False otherwise.
        pass

    def get_available_categories(self):
        """Return a list of categories that have not yet been used."""
        available = []

        # TODO: Add every category whose score is None.

        return available

    def total_score(self):
        """Return the total of all completed categories."""
        total = 0

        # TODO: Add all numeric scores while ignoring None.

        return total

    def save_to_file(self, filename):
        """Write the scorecard to a text file."""
        # TODO:
        # Open filename in write mode.
        # Write a heading.
        # Write each category and score.
        # Write the total score.
        #
        # Use:
        # with open(filename, "w") as file:
        #     ...
        pass
