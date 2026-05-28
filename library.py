import random

def gen_random_int(number: int, seed: int) -> list[int]:
    ### your code ###
    result = None
    random.seed(seed)
    result = range(0, number)
    result = list(result)
    random.shuffle(result)


def create_string(array: list[int]) -> str:
    ### your code ###
    n = len(array)
    result = ""
    for i in range (0, n):
        result += str(array[i])
        if i != n-1:
            result += ", "
        else:
            result += "."
    return result



def my_sort(array):
    ### your code ###
    # insertion sort

    n = len(array)
    for outer_index in range(1, n):
        inner_index = outer_index
        while inner_index > 0 and array[inner_index] < array[inner_index - 1]:
            first_number = array[inner_index - 1]
            second_number = array[inner_index]
            array[inner_index - 1] = second_number
            array[inner_index] = first_number
            inner_index -= 1
