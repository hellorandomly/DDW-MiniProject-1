import streamlit as st
import pandas as pd
from library import create_string

st.set_page_config(
    page_title="Exercise 3"
)

st.markdown(
    """
    <style>
    .stApp {
        background-color: #F1F4F9;
    }

    h2 {
        color: #263238 !important;
        font-family: 'Segoe UI';
        font-weight: 700 !important;
        text-align: center;
        margin-bottom: 5px !important;
    }

    div[data-baseweb="input"], 
    div[data-baseweb="input"] input {
        background-color: #FFFFFF !important;
    }

    div[data-baseweb="input"] {
        border-radius: 10px !important;
        border: 2px solid #90CAF9;
        background-color: #FFFFFF;
    }

    button[data-testid="stBaseButton-secondary"] {
        background-color: #0087B7 !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 0.5rem 1rem !important;
        font-weight: 500 !important;
        font-size: 16px !important;
        width: 100% !important;
        transition: background-color 0.2s ease;
    }
    """,
    unsafe_allow_html=True
)

st.header("Product Spreadsheet")

def clear():
    st.session_state['data'] = []

def cycle_sort_strings(arr):
    n = len(arr)
    
    for cycle_start in range(0, n - 1):
        item = arr[cycle_start]
        
        pos = cycle_start
        # Cycle_start + 1, because anything behind is already
        # in the right place (as a result of a previous cycle)
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
            # Range starts from cycle_start + 1, because the new 'item'
            # is guaranteed to be less than the cycle_start value since they swapped
            for i in range(cycle_start + 1, n):
                if arr[i] < item:
                    pos += 1

            # No same position check needed

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
        st.session_state.error = 'Please enter the ID!'
        return
    if st.session_state.name == "":
        st.session_state.error = 'Please enter the name!'
        return

    # Extract existing IDs to check for duplicates
    existing_ids = [item["ID"] for item in st.session_state.data]
    if st.session_state.id in existing_ids:
        st.session_state.error = 'ID already exists!'
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


col1, = st.columns(1)

with col1:
    if st.button("Add", width='stretch'):
        submit()

if st.session_state.error:
    st.error(st.session_state.error)

col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("Sort by ID", width='stretch'):
        sort_outer_ls("ID")
with col2:
    if st.button("Sort by name", width='stretch'):
        sort_outer_ls("Name")
with col3:
    if st.button("Sort by Price", width='stretch'):
        sort_outer_ls("Price")
with col4:
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
        st.image(item["Image"], width='stretch')
        st.write(f"**{item['Name']}**")
        st.caption(f"ID: {item['ID']} | ${item['Price']:.2f}")