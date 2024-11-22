from cooling_room import CoolingRoom, Compressor, Door, Food
from thermostat import (
    SimpleThermostat,
    LocalAverageThermostat,
    CombinatoricSmartThermostat,
    FutureMinAverageThermostat,
)
from simulator import CoolerSimulator
import pandas as pd


def main():
    prices = pd.read_csv("elpris.csv")["Pris"]
    room = CoolingRoom(
        compressor=Compressor(electric_prices=prices),
        thermostat=CombinatoricSmartThermostat(electric_prices=prices),
        food=Food(),
        door=Door(),
        temp=5,
    )
    simulator = CoolerSimulator(room)
    res = simulator.simulate()
    print(res)


if __name__ == "__main__":
    main()
