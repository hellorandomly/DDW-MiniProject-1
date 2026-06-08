import streamlit as st
import pandas as pd
from library import create_string

st.set_page_config(
    page_title="Exercise 3"
)

st.header("Exercise 3")

def clear():
    st.session_state['data'] = []

def cycle_sort_strings(arr):
    n = len(arr)
    
    for cycle_start in range(0, n - 1):
        item = arr[cycle_start]
        
        pos = cycle_start
        for i in range(cycle_start + 1, n):
            if arr[i] < item:
                pos += 1
        
        # Terminate if in right position
        if pos == cycle_start:
            continue
        
        # Place behind duplicates
        while item == arr[pos]:
            pos += 1
        
        if pos != cycle_start:
            arr[pos], item = item, arr[pos]
            
        while pos != cycle_start:
            # Code is similar to the code under the outermost for loop
            # Terminates only when pos ends when cycle_start is replaced

            pos = cycle_start
            for i in range(cycle_start + 1, n):
                if arr[i] < item:
                    pos += 1
                    
            while item == arr[pos]:
                pos += 1
                
            if item != arr[pos]:
                arr[pos], item = item, arr[pos]
                
def sort_outer_ls(sort_by):
    list_of_lists = st.session_state.data

    # Gets the sort_by value for ever sublist (generates 1D list)
    strings_to_sort = [row[sort_by] for row in list_of_lists]
    
    # Makes a copy (for reference)
    original_strings = list(strings_to_sort)
    
    cycle_sort_strings(strings_to_sort)
    
    sorted_outer = []
    for sorted_str in strings_to_sort:

        # Find the earliest reference
        orig_index = original_strings.index(sorted_str)
        
        sorted_outer.append(list_of_lists[orig_index])
        
        # Prevent this index from being used again
        original_strings[orig_index] = None

    st.session_state.data = sorted_outer

if 'id' not in st.session_state:
        st.session_state.id = ''
if 'name' not in st.session_state:
        st.session_state.name = ''
if 'error' not in st.session_state:
        st.session_state.error = None
if 'data' not in st.session_state:
        st.session_state.data = []

def submit():
    if st.session_state.id == "":
        st.error('Please enter the ID!')
        return
    if st.session_state.name == "":
        st.error('Please enter the Name!')
        return
    if st.session_state.id in [sublist[0] for sublist in st.session_state.data]:
        st.error('ID already exists!')
        return

    st.session_state.error = None
    st.session_state.data.append([st.session_state.id, st.session_state.name])

col1, col2 = st.columns(2)

with col1:
    st.text_input("Enter ID:", key="id")
with col2:
    st.text_input("Enter Name:", key="name")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Add", width='stretch'):
        submit()
with col2:
    if st.button("Sort by ID", width='stretch'):
        sort_outer_ls(0)
with col3:
    if st.button("Sort by name", width='stretch'):
        sort_outer_ls(1)
with col4:
    if st.button("Clear", width='stretch'):
        clear()

st.dataframe(pd.DataFrame(st.session_state['data'], columns=['ID', 'Name']))