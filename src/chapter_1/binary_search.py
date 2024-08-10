from typing import Any


def binary_search(data: list, item: Any) -> int | None:
    """
    Алгоритм бинарного поиска

    Args:
        data(list): упорядоченный массив(array)
        item(Any): искомое значение
    Returns:
        result(int): индекс искомого значения item
        None: в случае отсутствия item в data
    """
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = data[mid]

        if guess == item:
            return mid

        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 3, 5, 7, 9]

if __name__ == '__main__':
    print(binary_search(my_list, 3))
    print(binary_search(my_list, -1))
