from abc import ABC, abstractmethod
from cooling_room import CoolingRoom
import pandas as pd


class Thermostat(ABC):
    def __init__(self) -> None:
        self.cooling_room: CoolingRoom | None = None

    def register(self, room: "CoolingRoom") -> None:
        """
        Register the thermostat in the room
        :param room: CoolingRoom to register the thermostat
        :return: None
        """
        assert isinstance(room, CoolingRoom), "The thermostat can only be registered in a CoolingRoom"
        self.cooling_room = room

    @abstractmethod
    def recommended_compressor_state(self, i: int) -> bool:
        """
        Return the recommended state of the compressor
        :param i: The current iteration step
        :return: True if the compressor should be on, False otherwise
        """
        if not self.cooling_room:
            raise ValueError("The thermostat is not registered in any room")


class SimpleThermostat(Thermostat):
    def __init__(self, target_temp: int = 5) -> None:
        super().__init__()
        self.target_temp = target_temp

    def recommended_compressor_state(self, i: int) -> bool:
        super().recommended_compressor_state(i)
        return self.cooling_room.temp > self.target_temp


class LocalAverageThermostat(Thermostat):
    def __init__(self, electric_prices: pd.Series = None) -> None:
        super().__init__()
        self.electric_prices = electric_prices

    def recommended_compressor_state(self, i: int) -> bool:
        super().recommended_compressor_state(i)
        if self.electric_prices is None:
            raise ValueError("Electric prices not set")

        current_price = self.electric_prices.iloc[i]
        local_avg = self.electric_prices.iloc[max(0, i - 5):min(i+5, len(self.electric_prices)-1)].mean()

        if self.cooling_room.temp >= 6.4:
            return True

        if current_price <= local_avg and self.cooling_room.temp > 4:
            return True

        return False


class FutureMinAverageThermostat(Thermostat):
    def __init__(self, electric_prices: pd.Series = None) -> None:
        super().__init__()
        self.electric_prices = electric_prices

    def recommended_compressor_state(self, i: int) -> bool:
        super().recommended_compressor_state(i)
        if self.electric_prices is None:
            raise ValueError("Electric prices not set")

        current_price = self.electric_prices.iloc[i]
        near_future_min = self.electric_prices.iloc[
            min(i+1, len(self.electric_prices)-1):min(i+3, len(self.electric_prices)-1)
        ].min()

        if self.cooling_room.temp >= 6.4:
            return True

        if self.cooling_room.temp > 5:
            return current_price <= near_future_min

        return False


class CombinatoricSmartThermostat(Thermostat):
    def __init__(self, electric_prices: pd.Series = None) -> None:
        super().__init__()
        self.electric_prices = electric_prices

    def recommended_compressor_state(self, i: int) -> bool:
        super().recommended_compressor_state(i)
        if self.electric_prices is None:
            raise ValueError("Electric prices not set")

        current_price = self.electric_prices.iloc[i]
        local_avg = self.electric_prices.iloc[max(0, i - 5):min(i+5, len(self.electric_prices)-1)].mean()
        near_future_min = self.electric_prices.iloc[
            min(i+1, len(self.electric_prices)-1):min(i+3, len(self.electric_prices)-1)
        ].min()

        if self.cooling_room.temp >= 6.4:
            return True

        if self.cooling_room.temp > 5.8:
            return current_price <= near_future_min

        if current_price <= local_avg and self.cooling_room.temp > 4:
            return True

        return False
