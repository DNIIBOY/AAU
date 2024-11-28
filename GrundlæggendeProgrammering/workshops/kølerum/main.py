from cooling_room import CoolingRoom, Compressor, Door, Food
from thermostat import SimpleThermostat, CombinatoricSmartThermostat
from simulator import CoolerSimulator
from dataplotter import DataPlotter
import pandas as pd


def optimize_simple_thermostat() -> None:
    prices = pd.read_csv("elpris.csv")["Pris"]

    cheapest_cost = float("inf")
    best_temp = 0
    for target_temp in range(35, 85):
        thermostat = SimpleThermostat(target_temp=target_temp/10)
        room = CoolingRoom(
            compressor=Compressor(electric_prices=prices),
            thermostat=thermostat,
            food=Food(),
            door=Door(),
            temp=5,
        )
        simulator = CoolerSimulator(room)
        res = simulator.simulate()
        total_cost = res["Total Cost"].iloc[-1]
        if total_cost < cheapest_cost:
            cheapest_cost = total_cost
            best_temp = target_temp

    print("Best temperature:", best_temp/10)


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
    plotter = DataPlotter(res)
    plotter.plot_prices()


if __name__ == "__main__":
    main()
