import tkinter as tk
from matplotlib import pyplot as plt
from simulator import HopHopSimulator
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.configure(bg="#111827")
        self.title("Kanin Hop Hop Simulator")
        self.geometry("600x400")
        self.resizable(False, False)
        tk.Label(
            self,
            text="Kanin Hop Hop Simulator",
            foreground="#EF4444",
            bg="#111827",
            font=("Arial", 28, "bold")
        ).pack()

        iterations = tk.Frame(self, bg="#111827")
        iterations.pack(anchor="w", padx=8)
        tk.Label(
            iterations,
            text="Iterationer",
            foreground="#E5E7EB",
            bg="#111827",
            font=("Arial", 18),
            padx=20
        ).pack(side="left")
        tk.Entry(
            iterations,
            font=("Arial", 24),
            justify="right",
            width=5,
            bg="#1F2937",
            fg="#E5E7EB"
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
        ).pack(side="left")
        tk.Entry(
            player_count,
            font=("Arial", 24),
            justify="right",
            width=5,
            bg="#1F2937",
            fg="#E5E7EB"
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
        ).pack(side="left")

        radio_frame = tk.Frame(rules_frame, bg="#111827")
        radio_frame.pack(side="left")
        self.radio_buttons = [  # No need to use actual radiobuttons, because tkinter is weird
            tk.Button(
                radio_frame,
                text="Standard",
                background="#111827",
                foreground="#E5E7EB"
            ),
            tk.Button(
                radio_frame,
                text="Hurtig",
                background="#111827",
                foreground="#E5E7EB"
            ),
            tk.Button(
                radio_frame,
                text="Langsom",
                background="#111827",
                foreground="#E5E7EB"
            )
        ]
        for button in self.radio_buttons:
            button.config(command=lambda arg=button: self._handle_radio_click(arg))
            button.pack(side="left")
        tk.Button(
            self,
            text="Start",
            bg="#EF4444",
            fg="#E5E7EB",
            font=("Arial", 18),
            command=self.run_simulation
        ).pack()

    def _handle_radio_click(self, button):
        for b in self.radio_buttons:
            b.config(bg="#1F2937")
        button.config(bg="#EF4444")

    def run_simulation(self) -> None:
        simulator = HopHopSimulator(4)
        results = simulator.generate_win_rates(1000)
        self.plot_results(results)

    def plot_results(self, results: list[list[float]]) -> None:
        fig = Figure(figsize=(5, 5), dpi=100)
        plot1 = fig.add_subplot(111)
        for i, graph_data in enumerate(results):
            plot1.plot(graph_data, label=f"Player {i+1}")
        plot1.legend()
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()
