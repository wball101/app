import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import altair as alt



st.header('Display Text')
st.write('Hello, *World!* :sunglasses:')

st.write(1234)

df = pd.DataFrame({'first column': [1, 2, 3, 4],
                     'second column': [10, 20, 30, 40]})
st.write(df)

st.write('Below is a dataframe:', df, 'Above is a dataframe')

c = alt.Chart(df).mark_circle().encode(
    x='first column',y='second column', tooltip=['first column', 'second column'])
st.write(c)
