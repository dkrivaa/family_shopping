import streamlit as st
import pandas as pd

from repo_files import repofiles
from order import order

# Basic setup of page
st.set_page_config(page_title='The family shopping list', layout='wide')
st.markdown(f'<span style="color: #18448c; font-size: 32px"><b>Shopping list</b></span>'
         , unsafe_allow_html=True)
st.markdown('___')

# Getting sidebar order menu
order.order()

# Reading and showing present shopping list
df = repofiles.read_file()
table = st.table(df)


# Add action buttons
button_col1, button_col2, button_col3 = st.columns(3)

for i, row in df.iterrows():
    button_col1.button('Edit')
    button_col2.button('Delete')
    button_col3.checkbox('Select')

