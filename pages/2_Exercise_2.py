import streamlit as st
from library import create_string, my_sort

st.set_page_config(
    page_title="Exercise 2"
)

st.header("Exercise 2")


def sort_numbers():
    # TODO: Task 1
    #
    # Read the numbers entered by the user from session_state
    numbers: str = st.session_state.numbers

    # Create the list of integers from the string
    # array_int: list[int] = None

    # call my_sort() to sort the list of integers

    # call create_string() to convert the list to a single string
    # array_str: str = None

    # store into session_state

    ### your code ###

    numbers_int  = numbers.replace('.','')
    numbers_int = numbers_int.split(',')
    for i, num in enumerate(numbers_int):
        numbers_int[i] = int(num)
    my_sort(numbers_int)
    array_str: str = create_string(numbers_int)
    st.session_state['sorted_numbers'] = array_str


def clear():
    st.session_state['numbers'] = ""
    st.session_state['sorted_numbers'] = ""

if 'numbers' not in st.session_state:
    st.session_state.numbers = ""

if 'sorted_numbers' not in st.session_state:
    st.session_state.sorted_numbers = ""

st.text_input("Enter integers separated by comma:", key="numbers")

# TODO: Task 2
#
# Create a button which calls sort_numbers when it is clicked.
# st.button(something, on_click=something)

# Display the sorted_numbers from the session_state in this format:
# Sorted Numbers: ...
# st.write(your code here)

# Create a button which calls clear() when it is clicked
# st.button(your code here)

### your code ###
st.button("Sort", on_click=sort_numbers)
st.write("Sorted Numbers:", st.session_state['sorted_numbers'])
st.button("Clear", on_click=clear)