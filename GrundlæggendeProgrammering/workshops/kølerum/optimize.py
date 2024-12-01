from cooling_room import CoolingRoom, Compressor, Door, Food
from thermostat import SimpleThermostat, HysteresisThermostat
from simulator import CoolerSimulator
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
    print("Cheapest cost:", cheapest_cost)


def optimize_hystersis_thermostat() -> None:
    prices = pd.read_csv("elpris.csv")["Pris"]

    cheapest_cost = float("inf")
    best_temp = 0
    best_hysteresis = 0
    for target_temp in range(35, 85):
        for hysteresis in range(0, 10):
            thermostat = HysteresisThermostat(target_temp=target_temp/10, hysteresis=hysteresis/10)
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
                best_hysteresis = hysteresis

    print("Best temperature:", best_temp/10)
    print("Best hysteresis:", best_hysteresis/10)
    print("Cheapest cost:", cheapest_cost)


if __name__ == "__main__":
    optimize_hystersis_thermostat()
