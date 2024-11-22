from abc import ABC, abstractmethod
from cooling_room import CoolingRoom


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
