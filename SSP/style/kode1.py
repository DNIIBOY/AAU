import numpy as np


def pythagorean(a, b):
    return np.sqrt(a * a + b * b)


result = pythagorean(3, 4)
print(f"The diagonal is: {result}")
