import pandas as pd
from pathlib import Path
from matplotlib import pyplot as plt


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
