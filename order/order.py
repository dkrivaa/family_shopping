import streamlit as st
import pandas as pd

from repo_files import repofiles

def order_change():
    item = st.selectbox('Which order would you like to change?', df.index)
    choice = st.radio('What would you like to change?', ['Delete', 'Change Amount'])




