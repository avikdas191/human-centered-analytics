import streamlit as st
import pandas as pd

# Part 1

st.title("German Credit Data Explorer")

@st.cache_data
def load_data():
    df = pd.read_csv("german_credit_data_processed.csv")
    return df

df = load_data()

# Part 2

st.subheader("Data Preview")

all_columns = df.columns.tolist()
selected_columns = st.multiselect("Choose columns to display", all_columns, default=all_columns)

if selected_columns:
    st.dataframe(df[selected_columns].head())
else:
    st.warning("Please select at least one column.")

# Part 3

st.subheader("Bar Chart")

selected_col = st.selectbox("Choose a column", df.columns.tolist())

if df[selected_col].nunique() < 20:
    value_counts = df[selected_col].value_counts()
    st.bar_chart(value_counts)
else:
    st.warning("Too many values to display as a bar chart.")

# Part 4

st.subheader("Line Chart")

numeric_columns = df.select_dtypes(include='number').columns.tolist()
selected_numeric = st.multiselect("Choose numeric columns", numeric_columns, default=numeric_columns[:1])

if selected_numeric:
    st.line_chart(df[selected_numeric])
else:
    st.warning("Please select at least one numeric column.")

# Part 5

st.subheader("Correlation Table")

numeric_df = df.select_dtypes(include='number')
st.dataframe(numeric_df.corr())

# Bonus

st.sidebar.title("Controls")
st.sidebar.markdown("Use the widgets below to explore the data.")

with st.expander("Show Statistics"):
    st.dataframe(df.describe())