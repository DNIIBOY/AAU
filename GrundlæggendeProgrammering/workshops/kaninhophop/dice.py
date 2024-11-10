import random
from colors import RabitExitColor


class Dice:
    def __init__(self):
        self.options = [
            RabitExitColor.BLUE,
            RabitExitColor.GREEN,
            RabitExitColor.PURPLE,
            RabitExitColor.RED,
            RabitExitColor.YELLOW,
            None,  # Represents the roll "rabbit"
        ]

    def roll(self) -> RabitExitColor | None:
        """
        Roll the dice and return the result.
        :return: The result of the roll
        """
        choice = random.choice(self.options)
        return choice
