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

    for i in arr:
        if i == elem:
           return arr.index(i)
    return None
