from typing import Union


def binary_search(lst: list, guess: int) -> Union[None, int]:
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == guess:
            return mid
        elif lst[mid] < guess:
            low = mid + 1
        else:
            high = mid - 1
    return None


print(binary_search([1, 3, 54, 56, 745], 5612))
