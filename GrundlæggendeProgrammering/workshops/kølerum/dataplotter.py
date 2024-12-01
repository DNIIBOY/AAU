import pandas as pd
from pathlib import Path
from matplotlib import pyplot as plt
from typing import Iterable


class DataPlotter:
    def __init__(
        self,
        data: pd.DataFrame,
        plot_dir: str = "plots",
        prefix: str = ""
    ) -> None:
        self.data = data
        self.plot_dir = Path(plot_dir)
        self.prefix = prefix

        self.plot_dir.mkdir(exist_ok=True)  # Create the directory, if it doesn't exist

    def _slice(
        self,
        field: str,
        start: int | None = None,
        stop: int | None = None
    ) -> pd.Series:
        """
        Slice the data for a given field.
        :param field: Field to slice
        :param start: Start index of the data to slice
        :param stop: Stop index of the data to slice
        :return: pd.Series of the sliced data
        """
        if start is None:
            start = 0

        if stop is None:
            stop = len(self.data[field])

        return self.data[field][start:stop]

    def _save_plot(self, name: str) -> None:
        """
        Save the plot to the plot directory.
        :param name: Name of the plot
        :return: None
        """
        name = f"{name}.png"
        if self.prefix:
            name = f"{self.prefix}_{name}"

        plt.savefig(self.plot_dir / name)
        plt.close()

    def plot_temperature(self, start: int | None = None, stop: int | None = None) -> None:
        """
        Plot the temperature data.
        :param start: Start index of the data to plot
        :param stop: Stop index of the data to plot
        :return: None
        """
        data = self._slice("Temperature", start, stop)
        data.plot()
        plt.xlabel("Time")
        plt.ylabel("Temperature")
        plt.title("Temperature over time")
        self._save_plot("temperature")

    def plot_price(self, start: int | None = None, stop: int | None = None) -> None:
        """
        Plot the total price.
        :param start: Start index of the data to plot
        :param stop: Stop index of the data to plot
        :return: None
        """
        data = self._slice("Total Cost", start, stop)
        data.plot()
        plt.xlabel("Time")
        plt.ylabel("Price")
        plt.title("Price over time")
        self._save_plot("price")

    def plot_prices(self, include_total: bool = False, start: int | None = None, stop: int | None = None) -> None:
        """
        Plot the compressor and foodloss costs in the same plot.
        :param include_total: Include the total price in the plot
        :param start: Start index of the data to plot
        :param stop: Stop index of the data to plot
        :return: None
        """
        compressor = self._slice("Compressor Cost", start, stop)
        foodloss = self._slice("Food Losses", start, stop)

        if include_total:
            total = self._slice("Total Cost", start, stop)
            total.plot(label="Total")
        compressor.plot(label="Compressor")
        foodloss.plot(label="Food Loss")

        plt.xlabel("Time")
        plt.ylabel("Price")
        plt.title("Price over time")
        plt.legend()
        self._save_plot("prices")


class MultiPlotter(DataPlotter):
    def __init__(
        self,
        data: Iterable[pd.DataFrame],
        names: Iterable[str] = None,
        plot_dir: str = "plots",
        prefix: str = "multi"
    ) -> None:
        assert all(len(d) == len(data[0]) for d in data), "Dataframes must have the same length"
        if names is None:
            names = [f"Data {i+1}" for i in range(len(data))]
        assert len(names) == len(data), "Number of names must match the number of dataframes"
        super().__init__(data, plot_dir, prefix)
        self.names = names

    def _slice(
        self,
        field: str,
        start: int | None = None,
        stop: int | None = None
    ) -> tuple[pd.Series]:
        """
        Slice the data for a given field.
        :param field: Field to slice
        :param start: Start index of the data to slice
        :param stop: Stop index of the data to slice
        :return: pd.Series of the sliced data
        """
        if start is None:
            start = 0

        if stop is None:
            stop = len(self.data[0][field])

        return tuple(d[field][start:stop] for d in self.data)

    def plot_temperature(self, start: int | None = None, stop: int | None = None) -> None:
        """
        Plot the temperature data.
        :param start: Start index of the data to plot
        :param stop: Stop index of the data to plot
        :return: None
        """
        sliced = self._slice("Temperature", start, stop)
        for i, data in enumerate(sliced):
            data.plot(label=self.names[i])
        plt.xlabel("Time")
        plt.ylabel("Temperature")
        plt.title("Temperature over time")
        plt.legend()
        self._save_plot("temperature")

    def plot_price(self, start: int | None = None, stop: int | None = None) -> None:
        """
        Plot the total price.
        :param start: Start index of the data to plot
        :param stop: Stop index of the data to plot
        :return: None
        """
        sliced = self._slice("Total Cost", start, stop)
        for i, data in enumerate(sliced):
            data.plot(label=self.names[i])
        plt.xlabel("Time")
        plt.ylabel("Price")
        plt.title("Price over time")
        plt.legend()
        self._save_plot("price")

    def plot_prices(self, include_total: bool = False, start: int | None = None, stop: int | None = None) -> None:
        """
        Plot the compressor and foodloss costs in the same plot.
        :param include_total: Include the total price in the plot
        :param start: Start index of the data to plot
        :param stop: Stop index of the data to plot
        :return: None
        """
        sliced_compressor = self._slice("Compressor Cost", start, stop)
        sliced_foodloss = self._slice("Food Losses", start, stop)

        if include_total:
            sliced_total = self._slice("Total Cost", start, stop)
            for i, total in enumerate(sliced_total):
                total.plot(label=self.names[i])

        for i, compressor in enumerate(sliced_compressor):
            compressor.plot(label=self.names[i] + " Compressor")
        for i, foodloss in enumerate(sliced_foodloss):
            foodloss.plot(label=self.names[i] + " Food Loss")

        plt.xlabel("Time")
        plt.ylabel("Price")
        plt.title("Price over time")
        plt.legend()
        self._save_plot("prices")
