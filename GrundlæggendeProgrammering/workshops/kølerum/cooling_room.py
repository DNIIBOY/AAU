from typing import TYPE_CHECKING
from pandas import Series
from random import random
from math import exp

if TYPE_CHECKING:
    from thermostat import Thermostat  # Handle circular imports


class Door:
    def __init__(self, is_open: bool = False) -> None:
        self.is_open = is_open

    def shuffle(self) -> None:
        """
        10% Chance of the door being open
        :return: None
        """
        self.is_open = random() < 0.1


class Food:
    def __init__(self) -> None:
        self.losses = 0

    def deteriorate(self, temp: float, delta_t: int = 300) -> None:
        """
        Deteriorate the food based on the temperature
        :param temp: The current temperature
        :param delta_t: Amount of time passed since last update
        :return: None
        """
        if 3.5 <= temp < 6.5:
            # No deterioration between 3.5 and 6.5 degrees
            return

        if temp < 3.5:
            self.losses += (4.39 * exp(-0.49*temp)/300) * delta_t
            return

        if temp >= 6.5:
            self.losses += (0.11 * exp(0.31*temp)/300) * delta_t


class Compressor:
    def __init__(
        self,
        temp: float = -5,
        is_on: bool = False,
        electric_prices: Series = None
    ) -> None:
        self.temp = temp
        self.is_on = is_on
        self.cost = 0

        self._off_factor = 0
        self._on_factor = 8e-6

        self._electric_prices = electric_prices

    def consume_electricty(self, i: int) -> None:
        """
        Consume electricity and update the total price, if the compressor is on
        :param i: The current iteration step
        :return: None
        """
        if self._electric_prices is None:
            raise ValueError("Electric prices not set")

        if self.is_on:
            self.cost += float(self._electric_prices.iloc[i])

    @property
    def temp_factor(self) -> float:
        return self._on_factor if self.is_on else self._off_factor


class CoolingRoom:
    def __init__(
        self,
        compressor: Compressor,
        thermostat: "Thermostat",
        food: Food,
        door: Door,
        temp: float = 5
    ) -> None:
        self.compressor = compressor
        self.thermostat = thermostat
        self.thermostat.register(self)
        self.food = food
        self.door = door

        self.temp = temp

        self._ambient_temp = 20

        self._ambient_door_closed = 5e-7
        self._ambient_door_open = 3e-5

    @property
    def total_cost(self) -> float:
        return self.compressor.cost + self.food.losses

    def run(self, i: int) -> None:
        """
        Run the cooling room for the current iteration step
        :param i: The current iteration step
        :return: None
        """
        self.door.shuffle()
        self.compressor.is_on = self.thermostat.recommended_compressor_state(i)
        self.update_temp()
        self.compressor.consume_electricty(i)
        self.food.deteriorate(self.temp)

    def update_temp(
        self,
        delta_t: int = 300
    ) -> None:
        """
        Update the temperature of the room
        :param i: The current iteration step
        :param delta_t: Amount of time passed since last update
        :return: None
        """
        temp = self.temp

        if self.door.is_open:
            temp += self._ambient_door_open * (self._ambient_temp - self.temp) * delta_t
        else:
            temp += self._ambient_door_closed * (self._ambient_temp - self.temp) * delta_t

        temp += self.compressor.temp_factor * (self.compressor.temp - self.temp) * delta_t
        self.temp = temp
