def nested_sum(numbers: list) -> int:
    total = 0
    for n in numbers:
        if isinstance(n, list):
            total += nested_sum(n)
        else:
            total += n
    return total


def main() -> None:
    print(nested_sum([[[1, 2], [1, 2]], [[1, 2], [1, 2]]]))
    print(nested_sum([[[[[[[1]]]]]]]))
    print(nested_sum([[1, 2], [1, [1, 2], [1, 2, 3]], [1, [1, 2]]]))


if __name__ == "__main__":
    main()
