def get_float_value(prompt: str, err: str) -> float:
    for _ in range(3):
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print(err)

    print("Du har indtastet forkert 3 gange")
    exit()


height = get_float_value("Trekantens højde: ", "Højden skal være et tal")
base = get_float_value("Trekantens grundlinje: ", "Grundlinjen skal være et tal")

area = 0.5 * height * base

print("Arealet af trekanten er:", area)
print(f"Arealet kan udrengnes ved 1/2 * {height} * {base}")
