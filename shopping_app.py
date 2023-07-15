import streamlit as st
import pandas as pd


st.set_page_config(page_title='The family shopping list', layout='wide')
st.markdown(f'<span style="color: #18448c; font-size: 32px"><b>Shopping list</b></span>'
         , unsafe_allow_html=True)
st.markdown('___')

persons = ['Dad', 'Karen', 'Alex', 'Leanne', 'Yoel']

# New Order
person = st.selectbox('New order by:', persons)
product = st.text_input('What would you like to order?')
amount = st.selectbox('Amount', range(1, 10))

shopping = {'product': product, 'amount': amount, 'person': person}
