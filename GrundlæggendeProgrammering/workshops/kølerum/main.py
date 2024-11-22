from cooling_room import CoolingRoom, Compressor, Door, Food
from thermostat import SimpleThermostat
from simulator import CoolerSimulator
import pandas as pd


def main():
    prices = pd.read_csv("elpris.csv")["Pris"]
    room = CoolingRoom(
        compressor=Compressor(electric_prices=prices),
        thermostat=SimpleThermostat(target_temp=5),
        food=Food(),
        door=Door(),
        temp=5
    )
    simulator = CoolerSimulator(room)
    res = simulator.simulate()
    print(res)


if __name__ == "__main__":
    main()
