def purchase_beer(howmanybeers):
    print("You bought " + str(howmanybeers) + " amount of beers")


class AgeOutRangeError(Exception):
    "Raised when age is out of range"


def main():
    try:
        print("Bying beer...")
        user_age = int(input("How old are you? "))

        if user_age < 18:
            raise AgeOutRangeError("You cannot buy beer here - you are too young.")
        beer_count = int(input("how many? "))
        purchase_beer(beer_count)

    except AgeOutRangeError as exc:
        print(exc)

    except ValueError:
        print("Fuck dig din taber")
        return main()


if __name__ == "__main__":
    main()
