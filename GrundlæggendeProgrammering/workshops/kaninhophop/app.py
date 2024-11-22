import tkinter as tk
from simulator import HopHopSimulator
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from game import GameMode


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.iterations = tk.IntVar(value=1000)
        self.player_count = tk.IntVar(value=4)
        self.gamemode = GameMode.NORMAL

        self.plot = None
        self.configure(bg="#111827")
        self.title("Kanin Hop Hop Simulator")
        self.geometry("600x400")
        self.resizable(False, False)
        tk.Label(
            self,
            text="Kanin Hop Hop Simulator",
            foreground="#EF4444",
            bg="#111827",
            font=("Arial", 28, "bold"),
        ).pack()

        iterations = tk.Frame(self, bg="#111827")
        iterations.pack(anchor="w", padx=8)
        tk.Label(
            iterations,
            text="Iterationer",
            foreground="#E5E7EB",
            bg="#111827",
            font=("Arial", 18),
            padx=20,
            pady=40,
        ).pack(side="left")
        tk.Entry(
            iterations,
            font=("Arial", 24),
            justify="right",
            width=5,
            bg="#1F2937",
            fg="#E5E7EB",
            textvariable=self.iterations,
        ).pack(side="left")

        player_count = tk.Frame(self, bg="#111827")
        player_count.pack(anchor="w", padx=8)
        tk.Label(
            player_count,
            text="Antal spillere",
            foreground="#E5E7EB",
            bg="#111827",
            font=("Arial", 18),
            padx=20,
            pady=40,
        ).pack(side="left")
        tk.Entry(
            player_count,
            font=("Arial", 24),
            justify="right",
            width=3,
            bg="#1F2937",
            fg="#E5E7EB",
            textvariable=self.player_count,
        ).pack(side="left")

        rules_frame = tk.Frame(self, bg="#111827")
        rules_frame.pack(anchor="w", padx=8)
        tk.Label(
            rules_frame,
            text="Spilleregler",
            foreground="#E5E7EB",
            bg="#111827",
            font=("Arial", 18),
            padx=20,
            pady=30,
        ).pack(side="left")

        radio_frame = tk.Frame(rules_frame, bg="#111827")
        radio_frame.pack(side="left")
        self.radio_buttons = (
            [  # No need to use actual radiobuttons, because tkinter is weird
                tk.Button(
                    radio_frame,
                    text="Hurtig",
                    background="#111827",
                    foreground="#E5E7EB",
                ),
                tk.Button(
                    radio_frame,
                    text="Standard",
                    background="#EF4444",
                    foreground="#E5E7EB",
                ),
                tk.Button(
                    radio_frame,
                    text="Langsom",
                    background="#111827",
                    foreground="#E5E7EB",
                ),
            ]
        )
        for button in self.radio_buttons:
            button.config(command=lambda arg=button: self._handle_radio_click(arg))
            button.pack(side="left")
        tk.Button(
            self,
            text="Start",
            bg="#EF4444",
            fg="#E5E7EB",
            font=("Arial", 18),
            command=self.run_simulation,
        ).place(rely=0.9, relx=0.5, anchor="center")
        self.winner_text = tk.StringVar(value="")
        winner_label = tk.Label(
            background="#111827",
            foreground="#EF4444",
            font=("Arial", 18),
            textvariable=self.winner_text,
        )
        winner_label.place(relx=0.6, rely=0.9, anchor="w")

    def _handle_radio_click(self, button):
        for b in self.radio_buttons:
            b.config(bg="#1F2937")
        button.config(bg="#EF4444")
        self.gamemode = {
            "Hurtig": GameMode.QUICK,
            "Standard": GameMode.NORMAL,
            "Langsom": GameMode.SLOW,
        }[button["text"]]

    def run_simulation(self) -> None:
        """
        Run the simulation and plot the results.
        """
        simulator = HopHopSimulator(self.player_count.get(), self.gamemode)
        results = simulator.generate_win_rates(self.iterations.get())
        self.plot_results(results)

    def plot_results(self, results: list[list[float]]) -> None:
        """
        Plot the results of the simulation.
        :param results: A list of lists containing the win rates of each player.
        :return: None
        """
        fig = Figure(figsize=(5, 5), dpi=100)
        plot1 = fig.add_subplot(111)
        for i, graph_data in enumerate(results):
            plot1.plot(graph_data, label=f"Player {i+1}")

        last_round = [i[-1] for i in results]
        if all([0.30 <= x <= 0.45 for x in last_round]):
            ax = fig.gca()
            ax.set_ylim([0.25, 0.5])

        plot1.legend()
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        if self.plot:
            self.plot.destroy()
        self.plot = canvas.get_tk_widget()
        self.plot.place(relx=0.72, rely=0.4, width=320, height=200, anchor="center")
        win_rate = max(last_round)
        winner = last_round.index(win_rate) + 1
        self.winner_text.set(f"Spiller {winner} ({int(win_rate*100)}%)")


if __name__ == "__main__":
    app = App()
    app.mainloop()
