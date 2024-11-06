from game import Game
from game import GameMode


class HopHopSimulator:
    def __init__(self, player_count: int, gamemode: GameMode = GameMode.NORMAL) -> None:
        self.player_count = player_count
        self.gamemode = gamemode

    def run(self, iterations: int) -> list[list[bool]]:
        """
        Run the simulator for a given number of iterations.
        :param iterations: The number of iterations to run.
        :return: A list of lists, where the inner lists contain a boolean for each iteration indicating if the player
        won the game.
        """
        track_record = [[] for _ in range(self.player_count)]
        for _ in range(iterations):
            game = Game(self.player_count, mode=self.gamemode)
            winners = game.play()
            for starting_position in range(self.player_count):
                track_record[starting_position].append(starting_position in winners)
        return track_record

    def generate_win_rates(self, iterations: int) -> list[list[float]]:
        """
        Generate the win rate for each player.
        :param iterations: The number of iterations to run.
        :return: 2D list where the inner lists contain the win rate for each player.
        """
        track_record = self.run(iterations)
        win_rates = [[] for _ in range(self.player_count)]
        for starting_position in range(self.player_count):
            for iteration in range(len(track_record[starting_position])):
                win_rate = sum(track_record[starting_position][:iteration + 1]) / (iteration + 1)
                win_rates[starting_position].append(win_rate)
        return win_rates
