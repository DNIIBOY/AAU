def andengrad(a: float, b: float, c: float, include_calculations: bool) -> None:
    diskrimi = 0
    r1 = 0
    r2 = 0
    topx = 0
    topy = 0
    try:
        diskrimi = (b * b) - (4 * a * c)
        diskrimi_root = diskrimi ** 0.5
        r1 = (0 - b - diskrimi_root) / (2 * a)
        r2 = (0 - b + diskrimi_root) / (2 * a)
        topx = (0 - b) / (2 * a)
        topy = 0 - diskrimi / (4 * a)
    except (ValueError, ZeroDivisionError):
        print("Der er ingen løsninger")
        try:
            topx = (0 - b) / (2 * a)
            topy = 0 - diskrimi / (4 * a)
        except ZeroDivisionError:
            print("Der er ingen løsninger")

    if not include_calculations:
        print("Diskriminant: " + str(diskrimi))
        print("Toppunkt: " + str(round(topx, 2)) + ", " + str(round(topy, 2)))
        print("Rod 1: " + str(round(r1, 2)))
        print("Rod 2: " + str(round(r2, 2)))

    elif include_calculations:
        a = round(a, 4)
        b = round(b, 4)
        c = round(c, 4)
        print(f"""Diskriminant:
{b}² - (4 * {a} * {c}) = {round(diskrimi, 4)}""")
        print(f"""Rødder:
(-{b} + √({round(diskrimi, 4)}) / 2 * {a} = {round(r2, 4)}
(-{b} - √({round(diskrimi, 4)}) / 2 * {a} = {round(r1, 4)}""")
        print(f"""Toppunkt:
x = -{b} / 2 * {a} = {round(topx, 4)}
y = -{round(diskrimi, 4)} / 4 * {a} = {round(topy, 4)}""")
        print("""-----------------------------------------""")


def fixfloat(num):
    if "," in num:
        num = num.replace(",", ".")
    else:
        num = eval(num)  # Crazy unsafe, but ok for personal use i guess
    return float(num)


def take_input(value_name: str) -> float:
    value = input(f"            Indsæt {value_name} værdi: ")
    if value.casefold() == "q":
        exit(0)
    return fixfloat(value)


def main():
    while True:
        print("""----------Andengrads Funktioner----------
             Af: Daniel Nettelfield""")
        a = take_input("a")
        b = take_input("b")
        c = take_input("c")
        mellem = str(input("""Vil du have mellemregninger med? (j/n): """)).casefold()
        print("------------------------------------------")
        if mellem == "q":
            break

        if mellem not in ("j", "n"):
            print("Ugyldigt Input")
            continue
        include_calculations = mellem.casefold() == "j"
        andengrad(a, b, c, include_calculations)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Afslutter...")
        exit(0)
