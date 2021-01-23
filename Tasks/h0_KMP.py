from typing import Optional, List


def _prefix_fun(prefix_str: str) -> List[int]:
    """
    Prefix function for KMP

    :param prefix_str: substring for prefix function
    :return: prefix values table
    """

    P = [0] * len(prefix_str)
    j = 0
    i = 1

    while i < len(prefix_str):
        if prefix_str[j] != prefix_str[i]:
            if j > 0:
                j = P[j - 1]
            else:  # j == 0
                i += 1
        else:
            P[i] = j + 1
            i += 1
            j += 1
    return P


def kmp_algo(inp_string: str, substr: str) -> Optional[int]:
    """
    Implementation of Knuth-Morrison-Pratt algorithm

    :param inp_string: String where substr is to be found (haystack)
    :param substr: substr to be found in inp_string (needle)
    :return: index where first occurrence of substr in inp_string started or None if not found
    """

    i = 0  # Индекс строки
    j = 0  # Индекс подстроки
    prefix_value = _prefix_fun(substr)

    #inp_string - строка "abcaabca"
    #substr - подстрока  "abc"
    while i < len(inp_string): # Проходим всю строку
        if inp_string[i] == substr[j]: #Если совпадения в индексе, то прибавляем
            i += 1
            j += 1
            if j == len(substr): #Если индекс подстроки равен длине подстроки то возвращаем индекс строки минус размер подстроки
                return i - len(substr)
        elif j > 0: #Если индекс подстроки больше 0
            j = prefix_value[j - 1]
        else:
            i += 1

    return None
