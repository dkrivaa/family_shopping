import streamlit as st
import pandas as pd

from repo_files import repofiles
from order import order

# Basic setup of page
st.set_page_config(page_title='The family shopping list', layout='wide')
st.markdown(f'<span style="color: #18448c; font-size: 32px"><b>Shopping list</b></span>'
         , unsafe_allow_html=True)
st.markdown('___')

with st.container():
    col1, col2, col3 = st.columns([1, 1, 8])
    with col1:
        change_order = st.button('Change order')
    with col2:
        new_order = st.button('new order')

# Getting sidebar order menu
# order.order()

# Reading and showing present shopping list
df = repofiles.read_file()
table = st.table(df)

if change_order:
    change = st.selectbox('change order #:', df.index)
    st.write(change)
    order.order_change(change)

if new_order:
    order.new_order()


