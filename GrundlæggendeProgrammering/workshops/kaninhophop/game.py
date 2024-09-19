from rabitboard import RabitBoard
from dice import Dice


class Player:
    def __init__(self, starting_position: int = 0, rabbit_count: int = 0):
        self.rabbit_count = rabbit_count
        self.starting_position = starting_position


class Game:
    def __init__(self, player_count: int, rabbit_count: int = 20):
        self.player_count = player_count
        self.players = [Player(i) for i in range(player_count)]
        self.current_player = 0
        self.board = RabitBoard(rabbit_count)
        self.dice = Dice()

    def play(self) -> set[int]:
        """
        Play the game until a player wins.
        :return: The starting position of all winning players.
        """
        while self.board.rabit_count > 0:
            player = self.players[self.current_player]
            roll = self.dice.roll()
            took_rabbit = self.board.take_rabbit(roll)
            if took_rabbit:
                player.rabbit_count += 1

            self.current_player = (self.current_player + 1) % self.player_count

        max_count = max(self.players, key=lambda x: x.rabbit_count).rabbit_count
        return {player.starting_position for player in self.players if player.rabbit_count == max_count}
