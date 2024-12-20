from cooling_room import CoolingRoom, Compressor, Door, Food
from thermostat import Thermostat, SimpleThermostat, CombinatoricSmartThermostat, HysteresisThermostat, FutureMinAverageThermostat, LocalAverageThermostat
from simulator import CoolerSimulator
from dataplotter import DataPlotter, MultiPlotter
import pandas as pd


def create_room(thermostat: Thermostat, prices: pd.Series | None = None) -> CoolingRoom:
    if prices is None:
        prices = pd.read_csv("elpris.csv")["Pris"]

    room = CoolingRoom(
        compressor=Compressor(electric_prices=prices),
        thermostat=thermostat,
        food=Food(),
        door=Door(),
    )
    return room


def compare_thermostats() -> None:
    prices = pd.read_csv("elpris.csv")["Pris"]
    thermostats = [
        SimpleThermostat(6.2),
        CombinatoricSmartThermostat(electric_prices=prices),
    ]
    names = [
        "SimpleThermostat(6.2)",
        "CombinatoricThermostat",
    ]
    results = []
    for thermostat in thermostats:
        room = create_room(thermostat, prices)
        simulator = CoolerSimulator(room)
        results.append(simulator.simulate())

    plotter = MultiPlotter(
        data=results,
        names=names,
    )
    plotter.plot_temperature(stop=12*24)  # 24 hours


def main():
    prices = pd.read_csv("elpris.csv")["Pris"]
    room = CoolingRoom(
        compressor=Compressor(electric_prices=prices),
        thermostat=CombinatoricSmartThermostat(electric_prices=prices),
        food=Food(),
        door=Door(),
    )
    simulator = CoolerSimulator(room)
    res = simulator.simulate()
    print(res)
    plotter = DataPlotter(res)
    plotter.plot_prices()


if __name__ == "__main__":
    compare_thermostats()
