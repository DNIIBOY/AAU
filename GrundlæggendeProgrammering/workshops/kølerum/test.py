from unittest import TestCase, main
from unittest.mock import MagicMock
from cooling_room import Compressor, Door, Food, CoolingRoom
import pandas as pd


class TestDoor(TestCase):
    def setUp(self) -> None:
        self.door = Door()

    def test_shuffle(self) -> None:
        was_open = False
        for _ in range(100):
            self.door.shuffle()
            if self.door.is_open:
                was_open = True
                break

        self.assertTrue(was_open, "Door was not open 100 times in a row")


class TestFood(TestCase):
    def setUp(self) -> None:
        self.food = Food()

    def test_no_deterioration(self):
        self.food.deteriorate(5)
        self.assertEqual(self.food.losses, 0, "Food deteriorated when it should not have")

    def test_deterioration(self):
        self.food.deteriorate(10)
        self.assertNotEqual(self.food.losses, 0, "Food did not deteriorate")
        self.assertAlmostEqual(self.food.losses, 2.44, 1, "Food deteriorated the wrong amount")


class TestCompressor(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.prices = pd.read_csv("elpris.csv")["Pris"]

    def setUp(self) -> None:
        self.compressor = Compressor(electric_prices=self.prices)

    def test_temp_factor(self):
        self.compressor.is_on = False
        self.assertEqual(
            self.compressor.temp_factor,
            self.compressor._off_factor, "Temp factor is not off factor when off"
        )
        self.compressor.is_on = True
        self.assertEqual(
            self.compressor.temp_factor,
            self.compressor._on_factor,
            "Temp factor is not on factor when on"
        )

    def test_consume_no_electricity(self):
        self.compressor.is_on = False
        self.compressor.consume_electricty(0)
        self.compressor.consume_electricty(1)
        self.assertEqual(self.compressor.cost, 0, "Consumed electricity when off")

    def test_consume_electricity(self):
        self.compressor.is_on = True
        self.compressor.consume_electricty(0)
        self.compressor.consume_electricty(1)

        self.assertNotEqual(self.compressor.cost, 0, "Did not consume electricity when on")
        self.assertEqual(
            self.compressor.cost,
            self.prices[0] + self.prices[1],
            "Consumed the wrong amount of electricity",
        )


class TestCoolingRoom(TestCase):
    def setUp(self) -> None:
        self.compressor = MagicMock()
        self.thermostat = MagicMock()
        self.food = MagicMock()
        self.door = MagicMock()
        self.room = CoolingRoom(
            compressor=self.compressor,
            thermostat=self.thermostat,
            food=self.food,
            door=self.door,
            temp=5,
        )

    def test_setup(self) -> None:
        self.thermostat.register.assert_called_once_with(self.room)

    def test_total_cost(self) -> None:
        self.compressor.cost = 10
        self.food.losses = 5
        self.assertEqual(self.room.total_cost, 15, "Total cost is not the sum of compressor and food")

    def test_run(self) -> None:
        self.room.update_temp = MagicMock()
        self.room.run(0)
        self.door.shuffle.assert_called_once()
        self.thermostat.recommended_compressor_state.return_value = True
        self.thermostat.recommended_compressor_state.assert_called_once_with(0)
        self.assertTrue(self.compressor.is_on, "Compressor did not turn on")
        self.room.update_temp.assert_called_once()


if __name__ == "__main__":
    main()
