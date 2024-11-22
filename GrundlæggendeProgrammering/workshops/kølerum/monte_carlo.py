from cooling_room import CoolingRoom, Compressor, Door, Food
from thermostat import (
    SimpleThermostat,
    LocalAverageThermostat,
    CombinatoricSmartThermostat,
    FutureMinAverageThermostat,
)
from simulator import CoolerSimulator
import pandas as pd


def run_once(prices: pd.Series) -> float:
    room = CoolingRoom(
        compressor=Compressor(electric_prices=prices),
        thermostat=CombinatoricSmartThermostat(electric_prices=prices),
        food=Food(),
        door=Door(),
        temp=5,
    )
    simulator = CoolerSimulator(room)
    res = simulator.simulate()
    return res["Total Cost"].iloc[-1]


def main():
    prices = pd.read_csv("elpris.csv")["Pris"]
    runs = 100
    total_cost = 0
    for i in range(runs):
        if i % int((runs/100)) == 0:
            print(f"Progress: {int(i / runs * 100)+1}%")
        total_cost += run_once(prices)
    avg_cost = total_cost / runs
    print(f"Average cost: {avg_cost}")


if __name__ == "__main__":
    main()
