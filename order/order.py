import streamlit as st
import pandas as pd

from repo_files import repofiles


def order_change(item):
    choice = st.radio('What would you like to change?', ['Delete', 'Change Amount'])
    st.write(choice)




