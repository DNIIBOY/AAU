from unittest.mock import patch
import unittest


def checkInputValue(value) -> str:
    if value > 3:  # a
        if value >= 10:  # b
            print("Value is larger than or equal to 10")
        else:
            print("Value is larger than 3 and smaller than 10")
    else:
        if value > 0:  # c
            print("Value is between zero and three")
        else:
            print("Value is negative")


class TestCheckInputValue(unittest.TestCase):
    @patch("builtins.print")
    def test_negative_value(self, mock_print) -> None:
        checkInputValue(-5)
        mock_print.assert_called_once_with("Value is negative")

    @patch("builtins.print")
    def test_positive_small_value(self, mock_print) -> None:
        checkInputValue(2)
        mock_print.assert_called_once_with("Value is between zero and three")

    @patch("builtins.print")
    def test_medium_value(self, mock_print) -> None:
        checkInputValue(5)
        mock_print.assert_called_once_with("Value is larger than 3 and smaller than 10")

    @patch("builtins.print")
    def test_large_value(self, mock_print) -> None:
        checkInputValue(15)
        mock_print.assert_called_once_with("Value is larger than or equal to 10")

    def test_string_input(self) -> None:
        with self.assertRaises(TypeError):
            checkInputValue("abc")


if __name__ == "__main__":
    unittest.main()
