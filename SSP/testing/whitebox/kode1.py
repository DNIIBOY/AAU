import unittest


def checkInputValue(value) -> str:
    if value > 3:  # a
        if value >= 10:  # b
            print("Value is larger than or equal to 10")
            return "ab"
        else:
            print("Value is larger than 3 and smaller than 10")
            return "a"
    else:
        if value > 0:  # c
            print("Value is between zero and three")
            return "ac"
        else:
            print("Value is negative")
            return ""


valToBeChecked = 3
print("For value " + str(valToBeChecked))
checkInputValue(valToBeChecked)


class TestTheShit(unittest.TestCase):
    def test_rasmus_numbers(self) -> None:
        self.assertEqual(checkInputValue(-5), "")
        self.assertEqual(checkInputValue(-0.4), "")
        self.assertEqual(checkInputValue(0), "")
        self.assertEqual(checkInputValue(0.7), "ac")
        self.assertEqual(checkInputValue(-5), "")
        self.assertEqual(checkInputValue(-0.4), "")
        self.assertEqual(checkInputValue(1), "ac")
        self.assertEqual(checkInputValue(4), "a")
        self.assertEqual(checkInputValue(3452), "ab")


if __name__ == "__main__":
    unittest.main()
