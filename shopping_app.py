import streamlit as st
import pandas as pd

# Basic setup of page
st.set_page_config(page_title='The family shopping list', layout='wide')
st.markdown(f'<span style="color: #18448c; font-size: 32px"><b>Shopping list</b></span>'
         , unsafe_allow_html=True)
st.markdown('___')

# Who can order?
persons = ['Dad', 'Karen', 'Alex', 'Leanne', 'Yoel']

# New Order
st.sidebar.title('NEW ORDER')
person = st.sidebar.selectbox('New order by:', persons)
product = st.sidebar.text_input('What would you like to order?')
amount = st.sidebar.selectbox('Amount', range(1, 10))

shopping = {'product': product, 'amount': amount, 'person': person}

df = pd.DataFrame(shopping)

table = st.table(df)
