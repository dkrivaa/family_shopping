import streamlit as st
import pandas as pd

from repo_files import repofiles


def new_order():
    # Who can order?
    persons = ['Dad', 'Karen', 'Alex', 'Leanne', 'Yoel']
    # New Order
    st.sidebar.title('NEW ORDER')
    person = st.sidebar.selectbox('New order by:', persons)
    product = st.sidebar.text_input('What would you like to order?')
    amount = st.sidebar.selectbox('Amount', range(1, 10))

    product_list = []
    amount_list = []
    person_list = []

    shopping = {'product': product_list, 'amount': amount_list, 'person': person_list}
    return shopping


def order_change(change):
    pass




