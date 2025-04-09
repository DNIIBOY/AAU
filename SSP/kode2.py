def bubblesort(items: list[int]) -> list[int]:
    for i in range(0, len(items) - 1):
        swapped = False
        for j in range(len(items) - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if not swapped:
            break
    return items


items = [5, 3, 8, 6, 7, 2]
print("The unsorted list is: ", items)
print("The sorted list is: ", bubblesort(items))
