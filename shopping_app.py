import streamlit as st
import pandas as pd


st.set_page_config(page_title='The family shopping list', layout='wide')
st.markdown(f'<span style="color: #18448c; font-size: 32px"><b>Shopping list</b></span>'
         , unsafe_allow_html=True)
st.markdown('___')


persons = ['Karen', 'Alex', 'Leanne', 'Yoel' ]
st.selectbox('Ordered by:', (persons))

