import random

def gen_random_int(number: int, seed: int) -> list[int]:
    pass
    ### your code ###


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
    pass
