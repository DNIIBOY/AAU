# Energibesparende styring af kølerum

## Systemdiagram
Dette system gør brug af objektorienteret programmering (encapsulation, inheritance, polymorphism & abstraction).
Her gøres brug af abstract base classes og dependency injection som værktøjer til at skabe et modulært system, der giver mulighed for at eksperimentere med forskellige termostatløsninger, og simplificerer koden.

Klasserne er sammensat som på figuren herunder (hvis ikke den virker som forventet i light mode, så klik på den.)
<a href="https://app.eraser.io/workspace/cKjpT73Y5mQKIRYPADsD/preview?elements=d0-hJSrv-A1qdEQsqviBmA&type=embed"><img src="img/diagram.png"/></a>

## Abstract Base Classes
På systemdiagramet kan det ses at der gøres brug af dependecy injection til blandt andet at ændre hvilken thermostat systemet bruger, da man bare skal ændre hvilket objekt der bliver sat som termostat i `CoolingRoom` klassen.
Alle termostaterne inheriter fra klassen `Thermostat`, som er defineret således:

```python
class Thermostat(ABC):
    def __init__(self) -> None:
        self.cooling_room: CoolingRoom | None = None

    def register(self, room: "CoolingRoom") -> None:
        """
        Register the thermostat in the room
        :param room: CoolingRoom to register the thermostat
        :return: None
        """
        assert isinstance(
            room, CoolingRoom
        ), "The thermostat can only be registered in a CoolingRoom"
        self.cooling_room = room

    @abstractmethod
    def recommended_compressor_state(self, i: int) -> bool:
        """
        Return the recommended state of the compressor
        :param i: The current iteration step
        :return: True if the compressor should be on, False otherwise
        """
        if not self.cooling_room:
            raise ValueError("The thermostat is not registered in any room")
```
Her bliver alt der er tilfældes mellem alle termostater defineret.
Man kan se på første linje at `Thermostat` klassen inhertier fra `ABC` som er pythons indbyggede "Abstract Base Class", der beskriver klassen som "abstract", og giver adgang til at bruge `@abstractmethod` decoratoren.
Dette er meget lig andre objektorienterede programmeringssprog, der også har et `abstract` keyword, som fortæller at denne klasse ikke skal instantieres, men bare er et "blueprint" til de klasser der faktisk skal bruges.

For eksempel kan den simpleste termostat skrives med kun 7 linjer kode:
```python
class SimpleThermostat(Thermostat):
    def __init__(self, target_temp: int = 5) -> None:
        super().__init__()
        self.target_temp = target_temp

    def recommended_compressor_state(self, i: int) -> bool:
        super().recommended_compressor_state(i)
        return self.cooling_room.temp > self.target_temp
```
Her inheriter `SimpleThermostat` fra `Thermostat` og får derfor alt koden fra tidligere med.
Derudover tilføjes en target temperatur for termostaten, og `recommended_compressor_state` implementeres, så kompressoren tændes når temperaturen overstiger den tidligere definerede target temperatur.

## Kompressor
Kompressoren er implementeret som en klasse, der kan holde styr på sit eget energiforbrug, samt dens påvirkning på temperaturen.
Constructoren tager elpriserne, "køleværdien" af kompressoren $T_{komp} = -5$ samt startværdien (tændt/slukket) som argumenter.
```python
class Compressor:
    def __init__(
        self,
        electric_prices: pd.Series,
        temp: float = -5,
        is_on: bool = False
    ) -> None:
        self.temp = temp
        self.is_on = is_on
        self.cost = 0

        self._off_factor = 0
        self._on_factor = 8e-6

        self._electric_prices = electric_prices

    def consume_electricty(self, i: int) -> None:
        """
        Consume electricity and update the total price, if the compressor is on
        :param i: The current iteration step
        :return: None
        """
        if self.is_on:
            self.cost += float(self._electric_prices.iloc[i])

    @property
    def temp_factor(self) -> float:
        return self._on_factor if self.is_on else self._off_factor
```
Når `consume_electricty` kaldes, opdateres den totale udgift som kompressoren har haft. Hvis kompressoren er slukket ændres udgiften selvfølgelig ikke.
`Compressor` klassen har også en property `temp_factor`, som returnerer kompressorens nuværende effekt på totaltemperaturen, afhængigt af om den er tændt eller ej ($C_2$)

## CoolingRoom implementering
Selve `CoolingRoom` er selvfølgelig også implementeret som en klasse, der har alle de dependencies defineret i systemdiagramet.
Derudover kan man også definere starttemperaturen for rummet, som har defaultværdien $T[0] = 5$, og temperaturen udenfor kølerummet bliver defineret som en privat attribut $T_{rum} = 20$.
```python
class CoolingRoom:
    def __init__(
        self,
        compressor: Compressor,
        thermostat: "Thermostat",
        food: Food,
        door: Door,
        temp: float = 5,
    ) -> None:
        self.compressor = compressor
        self.thermostat = thermostat
        self.thermostat.register(self)
        self.food = food
        self.door = door

        self.temp = temp

        self._ambient_temp = 20
```
