import streamlit as st
from utils.data import load_data
from utils.config import ORDERS, COLORS
from utils.figures import plot_family_size, plot_outcome, plot_heatmap
df = load_data()

st.set_page_config(layout="wide")
st.title("Titanic Survival Prediction App")
st.caption("Data from https://www.kaggle.com/c/titanic/data")
st.image("utils/titanic.png")
st.sidebar.header("Filters")

show_data = st.sidebar.checkbox("Show sample data")
if show_data:
    st.dataframe(df, hide_index= True)

classes = st.sidebar.multiselect("Select classes", df["class"].unique(), default=df["class"].unique())
gender = st.sidebar.radio("Select gender", list(df["sex"].unique()) + ["All"], horizontal=True)

st.sidebar.markdown(
    "**Made by [Mohamed Khaled](https://www.linkedin.com/in/mohamedd11/)**"
)

if gender == "All":
    data = df[df["class"].isin(classes)]
else:
    data = df[(df["class"].isin(classes)) & (df["sex"] == gender)]

col1, col2, col3, col4 = st.columns(4)
col1.metric("Passengers", len(data), border=True)
col2.metric("Survival rate", f"{data["survived"].mean():.1%}", border=True)
col3.metric("Median age", f"{data['age'].median():.1f}", border=True)
col4.metric("Median Fare", f"${data['fare'].median():.2f}", border=True)

tab1, tab2 = st.tabs(["Family size vs outcome","Heatmap"])
with tab1:
    c1, c2 = st.columns(2)
    with c1:
        st.plotly_chart(plot_family_size(data))

    with c2:
        st.plotly_chart(plot_outcome(data))

with tab2:
    st.plotly_chart(plot_heatmap(data), use_container_width=True)
