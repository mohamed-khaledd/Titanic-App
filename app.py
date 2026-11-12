import streamlit as st
from utils.data import load_data
from utils.config import ORDERS, COLORS
from utils.figures import plot_family_size, plot_outcome
df = load_data()

st.set_page_config(layout="wide")
st.title("Titanic Survival Prediction App")
st.caption("Data from https://www.kaggle.com/c/titanic/data")
st.image("utils/titanic.png")

show_data = st.checkbox("Show sample data")
if show_data:
    st.dataframe(df, hide_index= True)

classes = st.multiselect("Select classes", df["class"].unique(), default=df["class"].unique())
gender = st.radio("Select gender", df["sex"].unique(), horizontal=True)

data = df[(df["class"].isin(classes)) & (df["sex"] == gender)]

c1, c2 = st.columns(2)
with c1:
    st.plotly_chart(plot_family_size(data))

with c2:
    st.plotly_chart(plot_outcome(data))
