import pandas as pd
import numpy as np
from cooling_room import CoolingRoom


class CoolerSimulator:
    def __init__(
        self, cooling_room: CoolingRoom, delta_t: int = 300, samples: int = 8640
    ) -> None:
        self.cooling_room = cooling_room
        self.delta_t = delta_t
        self.samples = samples

    def simulate(self) -> pd.DataFrame:
        columns = ["Temperature", "Compressor Cost", "Food Losses", "Total Cost", "Door"]
        data = np.zeros((self.samples, len(columns)))
        for i in range(self.samples):
            self.cooling_room.run(i)
            data[i] = [
                self.cooling_room.temp,
                self.cooling_room.compressor.cost,
                self.cooling_room.food.losses,
                self.cooling_room.total_cost,
                self.cooling_room.door.is_open,
            ]

        df = pd.DataFrame(data, columns=columns)
        return df
