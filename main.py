import streamlit as st
import os
from PIL import Image



# Create uploads directory if it doesn't exist
if not os.path.exists("uploads"):
    os.makedirs("uploads")

# File upload section
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    with open(os.path.join("uploads", uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.write("File saved successfully!")