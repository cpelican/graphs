# For 2 given strings
# take the min of the last 3 values(above current number, before, above and before)

# str_1: 'bao', str_2: 'cab
#       b  a  o
#    0  1  2  3
# c  1  1  2  3
# a  2  2  1  2
# b  3  2  2  2

# Example with this matrix:
# give each letter a number
# start iterating:
#   - look at precedent values, here 0,1,1, take the smallest, see if b and c are different, if so add 1 to 0
#   - continue iteration, the last number is the levenshtein distance
#       b  a  o           b  a  o           b  a  o               b  a  o
#    0  1  2  3        0  1  2  3        0  1  2  3            0  1  2  3
# c  1              c  1(0+1)         c  1  1(1+1)   (...)  c  1  1  2  3
# a  2              a  2              a  2                  a  2  2(1+0)
# b  3              b  3              b  3                  b  3

#  clear explanation here: https://stackabuse.com/levenshtein-distance-and-text-similarity-in-python/
from typing import List, Tuple

from src.heap import Heap


def levenshtein(str_1: str, str_2: str) -> int:
    """
    Function to calculate the levenshtein distance.
    with a matrix from the 2 strings, calculates the difference of each substring.
    """
    if len(str_1) == 0:
        return len(str_2)
    if len(str_2) == 0:
        return len(str_1)
    m = []
    if len(str_2) > len(str_1):
        str_1, str_2 = str_2, str_1

    for i in range(len(str_1) + 1):
        # Initialise the matrix
        if i == 0:
            m.append([j for j in range(len(str_2) + 1)])
            continue
        m.append([i] + [0] * len(str_2))
        # Fill the matrix
        for j in range(len(str_2) + 1):
            if j == 0:
                continue
            last_min = min(m[i-1][j], m[i][j-1], m[i-1][j-1])
            if str_1[i - 1] == str_2[j - 1]:
                m[i][j] = last_min
            else:
                m[i][j] = last_min + 1

    return m[len(str_1)][len(str_2)]


"""
SORTING ALGORITHMS
"""


def selection_sort(values: List[int]) -> List[int]:
    """
    The selection sort has a sub list of remaining items to sort, and an other one of sorted items.
    Complexity: O(n??2)
    """
    unsorted_list = [*values]
    sorted_list = []
    while len(unsorted_list) > 0:
        min, unsorted_list = get_min(unsorted_list)
        sorted_list.append(min)

    return sorted_list


def get_min(values: List[int]) -> Tuple[int, List[int]]:
    min_index = 0
    unsorted_list = [*values]
    for i, value in enumerate(values):
        if i == 0:
            continue
        if value < values[min_index]:
            min_index = i
    unsorted_list.pop(min_index)
    return values[min_index], unsorted_list


def bubble_sort(values: List[int]) -> List[int]:
    """
    The bubble sort algorithm sorts the elements by continuously swapping the elements when they are in the wrong order
    Complexity: O(n??2)
    """
    swap = True

    while swap is True:
        swap = False
        for i, value in enumerate(values):
            if i == len(values) - 1:
                break
            if value > values[i + 1]:
                temp = values[i]
                values[i] = values[i + 1]
                values[i + 1] = temp
                swap = True

    return values


def heap_sort(values: List[int]) -> List[int]:
    heap = Heap()
    sorted_values = []
    for value in values:
        heap.insert(f'node_{value}', value)
    while len(sorted_values) < len(values):
        name, value = heap.pop_min()
        sorted_values.append(value)

    return sorted_values


def merge(left_list: List[int], right_list: List[int]) -> List[int]:
    i = 0
    j = 0
    merged_list = []

    while True:
        if i == len(left_list):
            merged_list += right_list[j:]
            break
        if j == len(right_list):
            merged_list += left_list[i:]
            break
        if left_list[i] < right_list[j]:
            merged_list.append(left_list[i])
            i += 1
        else:
            merged_list.append(right_list[j])
            j += 1

    return merged_list


def merge_sort(values: List[int]) -> List[int]:
    if len(values) < 2:
        return values
    middle_i = len(values) // 2

    left = values[:middle_i]
    right = values[middle_i:]

    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    return merge(sorted_left, sorted_right)

