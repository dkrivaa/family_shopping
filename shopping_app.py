import streamlit as st
import pandas as pd

from repo_files import repofiles
from order import order

# Basic setup of page
st.set_page_config(page_title='The family shopping list', layout='wide',
                   initial_sidebar_state='collapsed')
st.markdown(f'<span style="color: #18448c; font-size: 32px"><b>Shopping list</b></span>'
         , unsafe_allow_html=True)
st.markdown('___')

df = repofiles.read_file()
df = df.rename_axis(index='Order ID')
st.markdown(f'<span style="color: #18448c; font-size: 18px"><b>Existing list</b></span>'
            , unsafe_allow_html=True)
table = st.dataframe(df)
st.markdown('___')

# CHANGING EXISTING ORDER
st.markdown(f'<span style="color: #18448c; font-size: 18px"><b>Change Order?</b></span>'
            , unsafe_allow_html=True)

item = st.selectbox('Which order would you like to change (order ID)?', df.index)
choice = st.radio('What would you like to change?', ['Delete', 'Amount'], index=1)

if choice == 'Delete':
    df = df.drop(item)
elif choice == 'Amount':
    new_amount = st.slider('new amount', 1, 10, 1)
    df.at[item, 'amount'] = new_amount
else:
    pass

submit = st.button('Submit changes', type='primary')
if submit:
    # Making sure all products are without spaces
    df['product'] = df['product'].str.replace(' ', '_')

    repofiles.del_file()
    repofiles.save_file(df)
    st.experimental_rerun()

st.markdown('___')
# NEW ORDER
st.markdown(f'<span style="color: #18448c; font-size: 18px"><b>New Order?</b></span>'
            , unsafe_allow_html=True)
# Who can order?
persons = ['Dad', 'Karen', 'Alex', 'Leanne', 'Yoel']
# New Order
product = st.text_input('What would you like to order?')
amount = st.selectbox('Amount', range(1, 10))
person = st.selectbox('New order by:', persons)
submit_order = st.button('Submit order', type='primary')

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
    st.experimental_rerun()







