import streamlit as st
import pandas as pd

from repo_files import repofiles
from order import order

# Basic setup of page
st.set_page_config(page_title='The family shopping list', layout='wide')
st.markdown(f'<span style="color: #18448c; font-size: 32px"><b>Shopping list</b></span>'
         , unsafe_allow_html=True)
st.markdown('___')

# SIDEBAR (NEW ORDER)
# Who can order?
persons = ['Dad', 'Karen', 'Alex', 'Leanne', 'Yoel']
# New Order
st.sidebar.title('NEW ORDER')
product = [st.sidebar.text_input('What would you like to order?')]
amount = [st.sidebar.selectbox('Amount', range(1, 10))]
person = [st.sidebar.selectbox('New order by:', persons)]
new_order = st.sidebar.button('SUBMIT')

change_order = st.button('Change order')

# Reading and showing present shopping list
df = repofiles.read_file()
table = st.table(df)




