import streamlit as st
import pandas as pd

from repo_files import repofiles
from order import order

# Basic setup of page
st.set_page_config(page_title='The family shopping list', layout='wide')
st.markdown(f'<span style="color: #18448c; font-size: 32px"><b>Shopping list</b></span>'
         , unsafe_allow_html=True)
st.markdown('___')

# EXISTING ORDER LIST
# Reading and showing present shopping list
df = repofiles.read_file()
table = st.table(df)


# SIDEBAR (NEW ORDER)
# Who can order?
persons = ['Dad', 'Karen', 'Alex', 'Leanne', 'Yoel']
# New Order
st.sidebar.title('NEW ORDER')
product = st.sidebar.text_input('What would you like to order?')
amount = st.sidebar.selectbox('Amount', range(1, 10))
person = st.sidebar.selectbox('New order by:', persons)
submit_order = st.sidebar.button('SUBMIT')

if ' ' in product:
    product = product.replace(' ', '_')

if submit_order:
    shopping = [product, amount, person]
    # shopping = {'product': product, 'amount': amount, 'person': person}
    df.loc[len(df.index)] = shopping

    # Making sure all products are without spaces
    df['product'] = df['product'].str.replace(' ', '_')

    repofiles.del_file()
    repofiles.save_file(df)

# CHANGING EXISTING ORDER
st.markdown(f'<span style="color: #18448c; font-size: 18px"><b>Change Order?</b></span>'
         , unsafe_allow_html=True)
choice = st.radio('What would you like to change?', ['Delete', 'Amount'])


if choice == 'Delete':
    item = st.selectbox('Which order would you like to change?', df.index)
    df = df.drop(item)

    # Making sure all products are without spaces
    df['product'] = df['product'].str.replace(' ', '_')

    repofiles.del_file()
    repofiles.save_file(df)






