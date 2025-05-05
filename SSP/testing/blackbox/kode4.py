import math
import random
import unittest


def mySqrt(number, guess, step, tol):
    if guess == 0:
        if number > 2:
            guess = 0.95 * number
        else:
            guess = number * 1.05
    tmp = guess * guess
    if (tmp - number) < tol:
        return guess
    else:
        if tmp < number:
            return mySqrt(number, (1 + step) * guess, step, tol)
        else:
            return mySqrt(number, (1 - step) * guess, step, tol)


def bubbleSort(arr):
    n = len(arr)
    swapped = False
    for i in range(n - 1):
        for j in range(0, n - 1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            return


def main():
    print("Give me a number :")
    number = input()

    myNumber = int(number)

    print("and the square root of this is: " + str(mySqrt(myNumber, 0, 0.01, 0.01)))
    print("compared with Pythons own algorithm: " + str(math.sqrt(myNumber)))
    print("Is this acceptable to you?")
    print("")

    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Now sorting the square numbers of : " + str(arr))
    arrSqrt = list(map(lambda x: mySqrt(x, 0, 0.01, 0.01), arr))
    bubbleSort(arrSqrt)
    print("sorted sqrt list: " + str(arrSqrt))

    arrSqrt2 = list(map(lambda x: math.sqrt(x), arr))
    arrSqrtSort2 = sorted(arrSqrt2)
    print("Squarerooted and sorted by Python: " + str(arrSqrtSort2))
    print("Is this acceptable to you?")


class BigBlackBox(unittest.TestCase):
    def own_version(self, numbers: list[int]) -> list[float]:
        arr_sqrt = list(map(lambda x: mySqrt(x, 0, 0.01, 0.01), numbers))
        bubbleSort(arr_sqrt)
        return arr_sqrt

    def python_version(self, numbers: list[int]) -> list[float]:
        return sorted(list(map(lambda x: math.sqrt(x), numbers)))

    def test_all(self) -> None:
        for _ in range(10):
            numbers = random.sample(range(1, 100), 10)
            own = self.own_version(numbers)
            python = self.python_version(numbers)
            for own_num, python_num in zip(own, python):
                self.assertAlmostEqual(
                    own_num,
                    python_num,
                    delta=0.1,
                    msg=f"Failed for numbers: {numbers}",
                )


if __name__ == "__main__":
    unittest.main()
