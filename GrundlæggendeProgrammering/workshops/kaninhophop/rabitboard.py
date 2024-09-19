from colors import RabitExitColor


class RabitExit:
    def __init__(self, has_rabit: bool = False):
        self.has_rabit = has_rabit


class RabitBoard:
    def __init__(self, rabit_count: int):
        self.rabit_count = rabit_count
        self.exits = {
            RabitExitColor.BLUE: RabitExit(),
            RabitExitColor.GREEN: RabitExit(),
            RabitExitColor.PURPLE: RabitExit(),
            RabitExitColor.RED: RabitExit(),
            RabitExitColor.YELLOW: RabitExit()
        }

    def __getitem__(self, item: RabitExitColor) -> RabitExit:
        return self.exits[item]

    def take_rabbit(self, color: RabitExitColor | None) -> bool:
        """
        Takes a rabbit from an exit.
        :param color: The color of the exit to take the rabbit from. If None, rabbit is taken from the board.
        :return: True if a rabbit was available to take at the specified exit, False otherwise.
        """
        if color is None:
            self.rabit_count -= 1
            return True

        if self.exits[color].has_rabit:
            self.exits[color].has_rabit = False
            return True

        # If there was no rabbit to take, move a rabbit to the exit
        self.exits[color].has_rabit = True
        self.rabit_count -= 1
        return False
