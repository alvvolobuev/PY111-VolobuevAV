"""
This module implements some functions based on linear search algo
Волобуев Алексаднр
"""
from typing import Sequence


def min_search(arr: Sequence) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers/ массив, содержащий числа
    :return: index of first occurrence of minimal element in array/ индекс первого вхождения минимального элемента в массив
    """

    min_index = arr.index(min(arr))

    return min_index
