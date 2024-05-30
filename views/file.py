import streamlit as st
import numpy as np
import pandas as pd

# Initialize 'dat' as an empty DataFrame
dat = pd.DataFrame()

def load_view():
    global dat
    uploaded_file = st.file_uploader("Choose a file", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file ,header=None)
        dat = pd.DataFrame(df)
        st.write("Data from the CSV file:")
        st.dataframe(dat)  # Display the DataFrame as an interactive table
    else:
        st.warning("No File attached")

def load_data():
    return dat





hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)