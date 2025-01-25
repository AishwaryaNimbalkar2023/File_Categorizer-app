import streamlit as st
from fileorganizer import organize_files
import os

# Function to navigate back to the parent directory
def get_parent_directory(current_dir):
    return os.path.abspath(os.path.join(current_dir, os.pardir))

# Initialize session state for tracking the directory
if "current_directory" not in st.session_state:
    st.session_state.current_directory = os.getcwd()  # Start with the current working directory

# App title
st.title("File Organizer")

# Display the current directory
st.write(f"### Current Directory: {st.session_state.current_directory}")

# Back button to navigate to the parent directory
if st.button("Go Back"):
    st.session_state.current_directory = get_parent_directory(st.session_state.current_directory)

# List files and subdirectories
items = os.listdir(st.session_state.current_directory)
subdirectories = [item for item in items if os.path.isdir(os.path.join(st.session_state.current_directory, item))]
files = [item for item in items if os.path.isfile(os.path.join(st.session_state.current_directory, item))]

# Show subdirectories in rows of 4
st.write("#### Subdirectories")
subdir_columns = st.columns(4)  # Create 4 columns for subdirectories
for index, subdir in enumerate(subdirectories):
    col = subdir_columns[index % 4]  # Distribute subdirectories evenly across the columns
    with col:
        if st.button(f"📂 {subdir}"):
            st.session_state.current_directory = os.path.join(st.session_state.current_directory, subdir)

# Show files in rows of 4
st.write("#### Files")
file_columns = st.columns(4)  # Create 4 columns for files
for index, file in enumerate(files):
    col = file_columns[index % 4]  # Distribute files evenly across the columns
    with col:
        st.write(f"📄 {file}")

# Button to organize files in the current directory
if st.button("Organize Files in Current Directory"):
    try:
        result = organize_files(st.session_state.current_directory)
        st.success("Files have been organized successfully!")
        st.text_area("Details", result, height=200)
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
