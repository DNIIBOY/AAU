import random
import unittest


def bubbleSort(arr):
    n = len(arr)

    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):

            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            return


class TestBubbleSort(unittest.TestCase):
    def test_bubblesort(self) -> None:
        arr = [64, 34, 25, 12, 22, 11, 90]
        correct = sorted(arr)
        bubbleSort(arr)
        self.assertEqual(arr, correct)

    def test_random(self) -> None:
        itertations = 100
        for i in range(itertations):
            with self.subTest(i=i):
                arr = list(random.sample(range(1000), 100))
                random.shuffle(arr)
                correct = sorted(arr)
                bubbleSort(arr)
                self.assertEqual(arr, correct)


if __name__ == "__main__":
    unittest.main()
