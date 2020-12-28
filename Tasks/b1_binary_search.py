# Волобуев Александр

from typing import Sequence, Optional

    
def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array/
    Выполняет двоичный поиск заданного элемента внутри массива

    :param elem: element to be found/
    элемент, который нужно найти
    :param arr: array where element is to be found/
    массив, в котором должен быть найден элемент
    :return: Index of element if it's presented in the arr, None otherwise/
    Индекс элемента, если он представлен в arr, не иначе
    """

    if not arr:
        return None

    middle = len(arr) // 2
    min_my = 0
    max_my = len(arr) - 1

    # You should return first occurrence from the array. 2 != 1
    # Вы должны вернуть первое вхождение из массива. 2 != 1

    while arr[middle] != elem and min_my <= max_my and middle != 1:
        if elem > arr[middle]:
            min_my = middle + 1
        else:
            max_my = middle - 1
        middle = (min_my + max_my) // 2

    if max_my < min_my:
        return None
    elif not middle % 2:
        middle //= 2
    else:
        return middle
