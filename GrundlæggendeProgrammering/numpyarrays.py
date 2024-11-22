import numpy as np
from matplotlib import pyplot as plt


def h(x):
    return 1 / (np.sqrt(2 * np.pi)) * np.exp(-0.5 * x**2)


def f(x):
    return 2 * x**2 - 10 * x + 12


def main():
    x = np.linspace(-4, 4, num=41)
    y = h(x)
    plt.plot(x, y)
    plt.show()


if __name__ == "__main__":
    main()
