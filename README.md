# Guided Lab: Build a Text-Based Yahtzee Game in Python

A solution by Alec Segur

https://github.com/21seguaj21/Data_Structures_Class_Yahtzee

## Overview

In this lab, you will build a **text-based Yahtzee game** using Python classes.

The project is designed to review and practice:

- classes and objects
- instance variables and methods
- lists
- dictionaries
- sets
- loops
- conditional statements
- functions
- user input
- exception handling
- importing classes from other files
- reading and writing text
- program organization

You will build the game in small stages. **Do not try to complete the entire game at once.**

---

# Final Goal

When finished, your game should allow one player to:

1. Roll five dice.
2. Keep selected dice.
3. Reroll the remaining dice.
4. Roll no more than three times per turn.
5. Choose a scoring category.
6. Record the score.
7. Prevent a category from being used twice.
8. Continue until all scoring categories have been used.
9. Display the final score.
10. Save the completed scorecard to a text file.

A turn might look something like this:

```text
Roll 1 of 3

1: [3]
2: [6]
3: [3]
4: [2]
5: [3]

Enter dice to KEEP (example: 1 3 5):
> 1 3 5

Roll 2 of 3

1: [3]
2: [4]
3: [3]
4: [6]
5: [3]

Enter dice to KEEP:
> 1 3 5

Roll 3 of 3

1: [3]
2: [3]
3: [3]
4: [5]
5: [3]

Choose a scoring category:
> Threes

You scored 12 points in Threes!
```

---

# Project Files

You will use the following files:

```text
yahtzee/
│
├── main.py
├── die.py
├── scorecard.py
└── yahtzee_game.py
```

Each file has a different responsibility.

### `die.py`

Contains the `Die` class.

A `Die` object knows:

- its current value
- how to roll itself

### `scorecard.py`

Contains the `ScoreCard` class.

A `ScoreCard` object knows:

- which categories are available
- which categories have already been used
- how to calculate scores
- how to calculate the total score
- how to save the scorecard to a text file

### `yahtzee_game.py`

Contains the `YahtzeeGame` class.

A `YahtzeeGame` object controls:

- the five dice
- turns
- rerolls
- user input
- category selection
- the scorecard

### `main.py`

Starts the program.

---

# Part 1 — The `Die` Class

Open `die.py`.

Your first task is to create a class representing one six-sided die.

A `Die` should have an instance variable:

```python
self.value
```

and methods:

```python
roll()
get_value()
```

## Requirements

### `__init__`

Set the initial value of the die.

### `roll`

Generate a random integer from 1 through 6 and store it in `self.value`.

You will need:

```python
import random
```

and:

```python
random.randint(1, 6)
```

### `get_value`

Return the current value.

## Test Your Class

Temporarily try:

```python
die = Die()

for i in range(10):
    die.roll()
    print(die.get_value())
```

You should see ten numbers between 1 and 6.

Do not continue until your `Die` class works.

---

# Part 2 — Create Five Dice

Open `yahtzee_game.py`.

The `YahtzeeGame` class should contain five `Die` objects.

Inside `__init__`, create:

```python
self.dice
```

as a list containing five dice.

One possible structure is:

```python
self.dice = []

for i in range(5):
    # create a Die and append it
```

Later, you may replace this with a list comprehension.

---

# Part 3 — Roll and Display Dice

Add the following methods to `YahtzeeGame`.

## `roll_all_dice`

Loop through `self.dice` and roll each object.

## `display_dice`

Display each die along with a position number.

Example:

```text
1: [4]
2: [1]
3: [6]
4: [4]
5: [2]
```

Remember:

- Python list indexes are `0, 1, 2, 3, 4`
- The player should see dice numbered `1, 2, 3, 4, 5`

Test these methods before moving on.

---

# Part 4 — Let the Player Keep Dice

After the first roll, the player should choose dice to keep.

For example:

```text
Enter dice to KEEP:
> 1 3 5
```

The input arrives as a string:

```python
"1 3 5"
```

You must convert it to something like:

```python
[1, 3, 5]
```

## Suggested Process

1. Use `input`.
2. Use `.split()`.
3. Convert each part to an integer.
4. Store the numbers in a list.

If the user simply presses Enter, treat that as keeping no dice:

```python
[]
```

---

# Part 5 — Reroll Unkept Dice

Create:

```python
reroll_dice(self, keep)
```

The parameter `keep` should be a list of die positions.

Example:

```python
keep = [1, 3, 5]
```

Dice 1, 3, and 5 should stay unchanged.

Dice 2 and 4 should be rolled again.

Be careful about the difference between a list index and the displayed die number.

---

# Part 6 — Input Validation

Your program should not crash if the player types invalid input.

For example:

```text
Enter dice to KEEP:
> dog
```

or:

```text
Enter dice to KEEP:
> 1 8
```

Use:

```python
try:
    ...
except ValueError:
    ...
```

Create a method:

```python
get_dice_to_keep()
```

It should continue asking until the user enters valid values from 1 through 5.

Optional challenge: prevent duplicate choices such as:

```text
1 1 3
```

---

# Part 7 — Build One Complete Turn

Create:

```python
play_turn()
```

A turn should:

1. Roll all five dice.
2. Display roll 1.
3. Allow the player to keep dice.
4. Reroll the others.
5. Display roll 2.
6. Allow the player to keep dice again.
7. Reroll the others.
8. Display roll 3.
9. Move to scoring.

A player may roll **at most three times**.

Once this works, you have completed the dice portion of the game.

---

# Part 8 — The `ScoreCard` Class

Open `scorecard.py`.

Create a dictionary named:

```python
self.scores
```

Use these categories:

```text
Ones
Twos
Threes
Fours
Fives
Sixes
Three of a Kind
Four of a Kind
Full House
Small Straight
Large Straight
Yahtzee
Chance
```

Initially, each category should have the value:

```python
None
```

For example:

```python
"Ones": None
```

## Why use `None`?

These two states are different:

```python
"Ones": None
```

means the category has **not been used**.

But:

```python
"Ones": 0
```

means the category **has been used and scored zero**.

---

# Part 9 — Display the Scorecard

Create:

```python
display()
```

Your output might look like:

```text
SCORE CARD
------------------------------
Ones                 3
Twos                 --
Threes               9
Fours                --
Fives                10
Sixes                --
Three of a Kind      --
Four of a Kind       --
Full House           25
Small Straight       --
Large Straight       --
Yahtzee              --
Chance               21
```

Display unused categories as:

```text
--
```

---

# Part 10 — Get the Dice Values

Your `YahtzeeGame` stores `Die` objects, but scoring is easier with integers.

For example, convert:

```text
Die, Die, Die, Die, Die
```

into:

```python
[3, 5, 3, 2, 3]
```

You can do this by calling `get_value()` on each die.

---

# Part 11 — Upper Section Scoring

Implement scoring for:

- Ones
- Twos
- Threes
- Fours
- Fives
- Sixes

For example:

```python
values = [3, 3, 6, 3, 1]
```

The score for Threes should be:

```text
9
```

Helpful list method:

```python
values.count(3)
```

---

# Part 12 — Count Matching Dice

Several Yahtzee categories depend on how many dice match.

For:

```python
[4, 4, 2, 4, 6]
```

you want to determine that:

```text
4 occurs 3 times
2 occurs 1 time
6 occurs 1 time
```

Write a helper method:

```python
get_counts(values)
```

A dictionary is a good choice.

For the example above, it could return:

```python
{
    4: 3,
    2: 1,
    6: 1
}
```

---

# Part 13 — Three of a Kind

A Three of a Kind contains at least three matching dice.

Example:

```text
3 3 3 5 6
```

The score is the sum of **all five dice**.

For this example:

```text
20
```

If there are not at least three matching dice, the score is `0`.

---

# Part 14 — Four of a Kind

A Four of a Kind contains at least four matching dice.

Example:

```text
5 5 5 5 2
```

The score is the sum of all five dice.

If the roll does not contain four matching dice, score `0`.

---

# Part 15 — Yahtzee

A Yahtzee means all five dice have the same value.

Example:

```text
6 6 6 6 6
```

Score:

```text
50
```

Otherwise score:

```text
0
```

A set may help.

For example:

```python
set([6, 6, 6, 6, 6])
```

becomes:

```python
{6}
```

---

# Part 16 — Full House

A Full House has:

- three of one number
- two of another number

Example:

```text
2 2 5 5 5
```

Score:

```text
25
```

One approach is to examine the values stored in the count dictionary.

---

# Part 17 — Small Straight

A Small Straight contains four consecutive numbers.

Possible small straights are:

```text
1 2 3 4
2 3 4 5
3 4 5 6
```

Score:

```text
30
```

Duplicates should not prevent a straight.

For example:

```text
1 2 3 3 4
```

still contains:

```text
1 2 3 4
```

A set is helpful here.

---

# Part 18 — Large Straight

A Large Straight is either:

```text
1 2 3 4 5
```

or:

```text
2 3 4 5 6
```

Score:

```text
40
```

Otherwise score `0`.

---

# Part 19 — Chance

Chance is simply the sum of all five dice.

Example:

```text
2 3 4 5 6
```

scores:

```text
20
```

---

# Part 20 — General Score Calculation

Create a method:

```python
calculate_score(self, category, values)
```

This method should:

1. receive the selected category
2. receive the five die values
3. determine the correct scoring rule
4. return the score

A large `if` / `elif` structure is acceptable.

Example:

```python
if category == "Ones":
    ...
elif category == "Twos":
    ...
```

---

# Part 21 — Record a Score

Create:

```python
record_score(self, category, values)
```

This method should:

1. make sure the category has not already been used
2. calculate the score
3. store it in `self.scores`
4. return or display the score

Once a category has been selected, it cannot be used again.

---

# Part 22 — Available Categories

Create:

```python
get_available_categories()
```

Return a list containing only categories whose scores are currently:

```python
None
```

For example:

```python
[
    "Twos",
    "Fours",
    "Sixes",
    "Yahtzee"
]
```

---

# Part 23 — Choose a Category

Back in `YahtzeeGame`, create:

```python
choose_category()
```

Display the available categories with numbers.

Example:

```text
Choose a category:

1. Ones
2. Twos
3. Threes
4. Fours
...
```

The user should type the number corresponding to the category.

Use input validation so the program does not crash if the user enters invalid data.

---

# Part 24 — Calculate the Total Score

Add:

```python
total_score()
```

to `ScoreCard`.

Add together all categories that have a numeric score.

Ignore categories whose value is still:

```python
None
```

---

# Part 25 — Add the ScoreCard to the Game

Inside `YahtzeeGame.__init__`, create a `ScoreCard` object.

Conceptually:

```text
YahtzeeGame
    |
    |---- five Die objects
    |
    +---- one ScoreCard object
```

This is called **composition**.

A `YahtzeeGame` **has a** `ScoreCard`.

A `YahtzeeGame` **has five** `Die` objects.

---

# Part 26 — Complete `play_turn`

Your complete `play_turn()` method should now:

1. perform up to three rolls
2. show the final dice
3. obtain the five numeric die values
4. ask the player for a scoring category
5. send the category and values to the `ScoreCard`
6. record the result

---

# Part 27 — The Full Game Loop

Create:

```python
play()
```

The game has 13 normal scoring categories, so the player should take 13 turns.

Each turn should:

1. display the turn number
2. display the current scorecard
3. call `play_turn()`

At the end:

1. display the completed scorecard
2. display the total score
3. save the scorecard to a text file

---

# Part 28 — Save the Scorecard to a Text File

Add:

```python
save_to_file(self, filename)
```

to `ScoreCard`.

Use:

```python
with open(filename, "w") as file:
```

The `"w"` means **write mode**.

Write a human-readable scorecard.

Example:

```text
YAHTZEE SCORE CARD
==============================

Ones                     3
Twos                     6
Threes                   9
Fours                    12
Fives                    15
Sixes                    18
Three of a Kind          20
Four of a Kind            0
Full House               25
Small Straight           30
Large Straight           40
Yahtzee                   0
Chance                   21

==============================
TOTAL SCORE:            199
```

Ask the player for a filename.

For example:

```text
Enter a filename for your scorecard:
> jesse_game1
```

If the user does not include `.txt`, you may add it automatically.

---

# Part 29 — `main.py`

Your `main.py` should be very small.

Its job is to:

1. import `YahtzeeGame`
2. create a game
3. start the game

Use:

```python
if __name__ == "__main__":
```

so that the program starts only when `main.py` is run directly.

---

# Testing Suggestions

Do not test the program only by playing a complete 13-turn game.

Test individual pieces.

## Test Dice

Can every die roll values from 1 to 6?

## Test Counts

Try:

```python
[4, 4, 2, 4, 6]
```

Does your count method correctly identify three `4`s?

## Test Yahtzee

Try:

```python
[5, 5, 5, 5, 5]
```

Expected score:

```text
50
```

## Test Full House

Try:

```python
[2, 2, 5, 5, 5]
```

Expected score:

```text
25
```

## Test Small Straight

Try:

```python
[1, 2, 3, 3, 4]
```

Expected score:

```text
30
```

## Test Large Straight

Try:

```python
[2, 3, 4, 5, 6]
```

Expected score:

```text
40
```

## Test Invalid Input

Try entering:

```text
dog
```

when a number is expected.

Your program should recover rather than crash.

---

# Class Design

As you work, think about which class should be responsible for each task.

## `Die`

Responsible for:

```text
dice behavior
```

Examples:

- storing a value
- rolling

## `ScoreCard`

Responsible for:

```text
scoring behavior
```

Examples:

- calculating categories
- remembering used categories
- totaling points
- writing the scorecard to a file

## `YahtzeeGame`

Responsible for:

```text
game behavior
```

Examples:

- controlling turns
- asking the user which dice to keep
- asking the user which category to choose
- displaying the game state

Keeping these responsibilities separate makes the program easier to understand and modify.

---

# Optional Extensions

If you finish early, consider adding one or more of the following:

- player name
- multiple players
- upper-section bonus
- Yahtzee bonus
- ASCII-art dice
- high-score file
- save and resume a game
- computer-controlled player
- unit tests
- colored terminal output
- custom exceptions
- inheritance with `HumanPlayer` and `ComputerPlayer`

Example future class structure:

```text
Player
  |
  +-- HumanPlayer
  |
  +-- ComputerPlayer
```

This would provide a natural use of inheritance and polymorphism.

---

# Submission Checklist

Before submitting, verify that:

- [ ] `Die` is implemented as a class.
- [ ] The game creates five `Die` objects.
- [ ] The player can roll up to three times.
- [ ] The player can keep selected dice.
- [ ] Invalid input does not crash the program.
- [ ] `ScoreCard` is implemented as a class.
- [ ] All 13 scoring categories work.
- [ ] A category cannot be used twice.
- [ ] The current scorecard can be displayed.
- [ ] The total score is calculated correctly.
- [ ] The full game lasts 13 turns.
- [ ] The final scorecard is saved to a `.txt` file.
- [ ] The program is divided into the required Python files.
- [ ] `main.py` starts the game.
