import streamlit as st
import pandas as pd

from repo_files import repofiles


def new_order():
    # Who can order?
    persons = ['Dad', 'Karen', 'Alex', 'Leanne', 'Yoel']
    # New Order
    st.sidebar.title('NEW ORDER')
    product = [st.sidebar.text_input('What would you like to order?')]
    amount = [st.sidebar.selectbox('Amount', range(1, 10))]
    person = [st.sidebar.selectbox('New order by:', persons)]
    return product, amount, person

    # shopping = {'product': product, 'amount': amount, 'person': person}
    # return shopping


def order_change(change):
    pass




