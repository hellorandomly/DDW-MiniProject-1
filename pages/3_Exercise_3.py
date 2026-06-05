import streamlit as st
from library import create_string

st.set_page_config(
    page_title="Exercise 3"
)

st.header("Exercise 3")

def clear():
    st.session_state['strings'] = ""
    st.session_state['sorted_strings'] = ""

def radix_sort_strings():
    strings: str = st.session_state.strings
    arr = strings.replace('.','')
    arr = arr.replace(' ','')
    arr = arr.split(',')

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
        
    array_str: str = create_string(arr)
    st.session_state['sorted_strings'] = array_str

if 'strings' not in st.session_state:
    st.session_state.strings = ""

if 'sorted_strings' not in st.session_state:
    st.session_state.sorted_strings = ""

st.text_input("Enter strings separated by comma:", key="strings")

st.button("Sort", on_click=radix_sort_strings)
st.write("Sorted Strings:", st.session_state['sorted_strings'])
st.button("Clear", on_click=clear)