import random

def gen_random_int(number: int, seed: int) -> list[int]:
    ### your code ###
    result = None
    random.seed(seed)
    result = range(0, number)
    result = list(result)
    random.shuffle(result)

    return result


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

def radix_sort_strings(arr):
    string_len = len(arr[0])
    
    for char_index in range(string_len - 1, -1, -1):
        n = len(arr)
        output = [""] * n
        count = [0] * 256

        for string in arr:
            char_code = ord(string[char_index]) 
            count[char_code] += 1

        for i in range(1, 256):
            count[i] += count[i - 1]

        for string_index in range(n - 1, -1, -1):
            char_code = ord(arr[string_index][char_index])
            output[count[char_code] - 1] = arr[string_index]
            count[char_code] -= 1

        for i in range(n):
            arr[i] = output[i]