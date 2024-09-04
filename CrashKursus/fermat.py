def get_float_value(prompt: str, err: str) -> float:
    for _ in range(3):
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print(err)

    print("Du har indtastet forkert 3 gange")
    exit()


def main():
    a = get_float_value("a: ", "a skal være et tal")
    b = get_float_value("b: ", "b skal være et tal")
    c = get_float_value("c: ", "c skal være et tal")
    n = get_float_value("n: ", "n skal være et tal")

    if a ** n + b ** n == c ** n:
        if n == 2:
            print("Yes, that does work!")
        else:
            print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")


if __name__ == "__main__":
    main()
