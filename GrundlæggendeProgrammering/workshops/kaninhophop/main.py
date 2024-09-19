from matplotlib import pyplot as plt
from simulator import HopHopSimulator


def main() -> None:
    simulator = HopHopSimulator(4)
    results = simulator.generate_win_rates(10000)

    # Plot each inner list on the same graph
    for i, graph_data in enumerate(results):
        plt.plot(graph_data, label=f"Player {i+1}")

    plt.title("Kanin Hop Hop Win Rate Over Time")
    plt.ylabel("Win Rate [%]")
    plt.xlabel("Starting Position")

    plt.legend()
    plt.savefig("output.png")


if __name__ == "__main__":
    main()
