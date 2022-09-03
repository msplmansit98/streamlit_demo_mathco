import streamlit as st
import pandas as pd
import numpy as np
import snowflake.connector
from home import data_fetcher

# def init_connection():
#     return snowflake.connector.connect(**st.secrets["snowflake"])

# conn = init_connection()

# @st.cache
# def data_fetcher():
#     query = '''SELECT * FROM cereals'''
#     cur = conn.cursor().execute(query)
#     df = pd.DataFrame.from_records(iter(cur), columns=[x[0] for x in cur.description])
#     return df





if not st.checkbox("Show Snowflake's data"):
    st.subheader('Table info:')
    df = data_fetcher()
    st.write(df)