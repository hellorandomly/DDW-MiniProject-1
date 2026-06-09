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
    list_of_dicts = st.session_state.data

    # Gets the sort_by value for ever sublist (generates 1D list)
    strings_to_sort = [row[sort_by] for row in list_of_dicts]
    
    # Makes a copy (for reference)
    original_strings = list(strings_to_sort)
    
    cycle_sort_strings(strings_to_sort)
    
    sorted_outer = []
    for sorted_str in strings_to_sort:

        # Find the earliest reference
        orig_index = original_strings.index(sorted_str)
        
        sorted_outer.append(list_of_dicts[orig_index])
        
        # Prevent this index from being used again
        original_strings[orig_index] = None

    st.session_state.data = sorted_outer

if 'id' not in st.session_state:
        st.session_state.id = ''
if 'name' not in st.session_state:
        st.session_state.name = ''
if 'price' not in st.session_state:
    st.session_state.price = 0.0
if 'error' not in st.session_state:
        st.session_state.error = None
if 'data' not in st.session_state:
    st.session_state.data = [
        {"ID": "101", "Name": "Bread", "Price": 2.50, "Image": "assets/bread.png"},
        {"ID": "102", "Name": "Milk", "Price": 3.20, "Image": "assets/milk.png"},
        {"ID": "103", "Name": "Eggs", "Price": 4.00, "Image": "assets/eggs.png"},
        {"ID": "104", "Name": "Apples", "Price": 5.50, "Image": "assets/apples.png"},
        {"ID": "105", "Name": "Bananas", "Price": 2.10, "Image": "assets/bananas.png"},
        {"ID": "106", "Name": "Yogurt", "Price": 3.00, "Image": "assets/yogurt.png"},
        {"ID": "107", "Name": "Rice", "Price": 12.00, "Image": "assets/rice.png"},
        {"ID": "108", "Name": "Pasta", "Price": 3.50, "Image": "assets/pasta.png"},
        {"ID": "109", "Name": "Cheese", "Price": 6.80, "Image": "assets/cheese.png"}
    ]


def submit():
    if st.session_state.id == "":
        st.error('Please enter the ID!')
        return
    if st.session_state.name == "":
        st.error('Please enter the Name!')
        return

    # Extract existing IDs to check for duplicates
    existing_ids = [item["ID"] for item in st.session_state.data]
    if st.session_state.id in existing_ids:
        st.error('ID already exists!')
        return

    st.session_state.error = None

    # Append as a dictionary
    st.session_state.data.append({
        "ID": st.session_state.id,
        "Name": st.session_state.name,
        "Price": st.session_state.price,
        "Image": "assets/placeholder.jpg"
    })

col1, col2, col3 = st.columns(3)

with col1:
    st.text_input("Enter ID:", key="id")
with col2:
    st.text_input("Enter Name:", key="name")
with col3:
    st.number_input("Enter Price:", key="price", min_value=0.0, format="%.2f")


col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("Add", width='stretch'):
        submit()
with col2:
    if st.button("Sort by ID", width='stretch'):
        sort_outer_ls("ID")
with col3:
    if st.button("Sort by name", width='stretch'):
        sort_outer_ls("Name")
with col4:
    if st.button("Sort by Price", width='stretch'):
        sort_outer_ls("Price")
with col5:
    if st.button("Clear", width='stretch'):
        clear()

st.dataframe(st.session_state.data)

st.divider()
st.subheader("Product Gallery")

# Filter out the manually added items (which have Image set to None)
gallery_items = st.session_state.data

# Create a 3-column layout
cols = st.columns(3)

# Loop through and draw the images
for index, item in enumerate(gallery_items):
    with cols[index % 3]:
        st.image(item["Image"], use_container_width=True)
        st.write(f"**{item['Name']}**")
        st.caption(f"ID: {item['ID']} | ${item['Price']:.2f}")