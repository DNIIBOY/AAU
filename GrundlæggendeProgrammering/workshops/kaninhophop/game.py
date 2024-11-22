from rabitboard import RabitBoard
from dice import Dice
from enum import Enum


class GameMode(Enum):
    QUICK = 0
    NORMAL = 1
    SLOW = 2


class Player:
    def __init__(self, starting_position: int = 0, rabbit_count: int = 0):
        self.rabbit_count = rabbit_count
        self.starting_position = starting_position


class Game:
    def __init__(
        self,
        player_count: int,
        rabbit_count: int = 20,
        mode: GameMode = GameMode.NORMAL,
    ):
        self.player_count = player_count
        self.players = [Player(i) for i in range(player_count)]
        self.current_player = 0
        self.mode = mode
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

            if self.mode == GameMode.SLOW and roll is None:  # Player loses a rabbit
                player.rabbit_count -= 1
                self.board.rabit_count += 1
            else:
                took_rabbit = self.board.take_rabbit(roll)
                if took_rabbit:
                    player.rabbit_count += 1

            if self.mode == GameMode.QUICK and roll is None:  # Player gets another turn
                continue
            self.current_player = (self.current_player + 1) % self.player_count

        max_count = max(self.players, key=lambda x: x.rabbit_count).rabbit_count
        return {
            player.starting_position
            for player in self.players
            if player.rabbit_count == max_count
        }
