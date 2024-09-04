def get_float_value(prompt: str, err: str) -> float:
    for _ in range(3):
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print(err)

    print("Du har indtastet forkert 3 gange")
    exit()


weight = get_float_value("Vægt: ", "Vægt skal være et tal")
height = get_float_value("Højde: ", "Højde skal være et tal")
if height > 100:
    height /= 100  # Expect cm if greater than 100

print(f"Vægt: {weight} kg")
print(f"Højde: {height} m")
print(f"Dit BMI er: {(weight)/(height**2)}")
