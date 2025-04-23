import unittest


def mySqrt(number, guess, step, tol):
    # We need to take out negative numbers...
    if number < 0:
        print("Error - we do not work with complex numbers here...")
        return -1

    # If we set guess to zero, we have to provide a number - we assume this is the initial call
    if guess == 0:
        if (
            number > 1
        ):  # If we have numbers larger than one, we can safely guess half as the sqrt
            guess = 0.5 * number
        else:
            guess = (
                number * 2
            )  # If we have numbers smaller than one, we need to double our guess

    tmp = guess * guess  # Now compute the square of our guess
    if (
        tmp - number
    ) < tol:  # Check if the (guess^2 - number) is lower than our tolerance level
        return guess
    else:
        if (
            tmp < number
        ):  # If our guess was too high, then iterate by calling ourselves again with a slightly lower guess
            return mySqrt(number, (1 + step) * guess, step, tol)
        else:  # Else, our guess was too small, we need to increase the guess for our next call
            return mySqrt(number, (1 - step) * guess, step, tol)


testVal = 9
print("Squareroot of " + str(testVal) + " is ")
print(mySqrt(testVal, 0, 0.001, 0.001))


class TestLort(unittest.TestCase):
    def test_sqrt(self) -> None:
        tolerance = 0.01
        self.assertEqual(mySqrt(-4, 0, 0.001, tolerance), -1)
        self.assertEqual(mySqrt(0, 0, 0.001, tolerance), 0)
        self.assertAlmostEqual(
            mySqrt(0.5, 0, 0.001, tolerance), 0.7071067811865476, delta=tolerance
        )
        self.assertAlmostEqual(mySqrt(1, 0, 0.001, tolerance), 1, delta=tolerance)
        self.assertAlmostEqual(mySqrt(3, 0, 0.001, tolerance), 1.5, delta=tolerance)
        self.assertAlmostEqual(mySqrt(9, 0, 0.001, tolerance), 3, delta=tolerance)
        self.assertAlmostEqual(mySqrt(34, 0, 0.01, tolerance), 5.8, delta=tolerance)


if __name__ == "__main__":
    unittest.main()
