import streamlit as st
import pandas as pd

from repo_files import repofiles
from order import order

# Basic setup of page
st.set_page_config(page_title='The family shopping list', layout='wide')
st.markdown(f'<span style="color: #18448c; font-size: 32px"><b>Shopping list</b></span>'
         , unsafe_allow_html=True)
st.markdown('___')

st.button('new order')

# Getting sidebar order menu
# order.order()

# Reading and showing present shopping list
df = repofiles.read_file()
table = st.table(df)

st.write(df)


editable_df = st.dataframe(df)

# Allow users to edit the DataFrame
if st.button('Apply Changes'):
    updated_data = {}
    for column in df.columns:
        updated_data[column] = []
        for row_value in editable_df[column]:
            if isinstance(row_value, str):
                updated_data[column].append(row_value)
            else:
                updated_data[column].append(row_value)

    df = pd.DataFrame(updated_data)




