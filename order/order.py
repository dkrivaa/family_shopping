import streamlit as st
import pandas as pd

from repo_files import repofiles

def order():
    # Who can order?
    persons = ['Dad', 'Karen', 'Alex', 'Leanne', 'Yoel']
    # New Order
    st.sidebar.title('NEW ORDER')
    person = st.sidebar.selectbox('New order by:', persons)
    product = st.sidebar.text_input('What would you like to order?')
    amount = st.sidebar.selectbox('Amount', range(1, 10))

    product_list = ['bamba']
    amount_list = [1]
    person_list = ['Dad']

    shopping = {'product': product_list, 'amount': amount_list, 'person': person_list}

    df = pd.DataFrame(shopping)
    repofiles.save_file(df)
