import streamlit as st
import pandas as pd
import numpy as np
import snowflake.connector
from matplotlib import pyplot as plt



def init_connection():
    return snowflake.connector.connect(**st.secrets["snowflake"])

conn = init_connection()

@st.cache
def data_fetcher():
    query = '''SELECT * FROM cereals'''
    cur = conn.cursor().execute(query)
    snowflake_data = pd.DataFrame.from_records(iter(cur), columns=[x[0] for x in cur.description])
    return snowflake_data


st.write('# Demo App')

st.write('## Popular Products: ')
option = st.selectbox(
     'Select the product type: ',
     data_fetcher().TYPE.unique())

st.write('Currently Selected:', option)

# df = data_fetcher().sort_values(by=['RATING'], ascending=False)
# df

df = data_fetcher()
df1 = df[df['TYPE']==option].sort_values(by=['RATING'], ascending=False).head(15)
st.bar_chart(data=df1, x='NAME', y='RATING', width=0, height=0, use_container_width=True)

