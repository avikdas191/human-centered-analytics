# %%
import streamlit as st
import pandas as pd

st.title("German Credit Data Explorer")

###################################################
################### Load the Data
###################################################

st.subheader("Part 1: Dataset Preview")


@st.cache_data
def load_data():
    return pd.read_csv("german_credit_data_processed.csv")


df = load_data()
st.success("German Credit Data loaded from local file!")

###################################################
################### Preview
###################################################

st.subheader("Part 2: Show a Preview")

st.write(df.head())

st.markdown("### Select Columns to Display")
columns = st.multiselect(
    "Choose columns", df.columns.tolist(), default=df.columns.tolist()
)
st.dataframe(df[columns])


###################################################
################### Bar Charts
###################################################

st.subheader("Part 3: Bar Chart Visualizations")

col = st.selectbox("Choose a column", df.columns)

if df[col].dtype == object or df[col].nunique() < 20:
    st.bar_chart(df[col].value_counts())
else:
    st.warning("Please select a categorical or low-cardinality column.")

###################################################
################### Line Charts
###################################################

st.subheader("Part 4: Line Charts")

num_cols = df.select_dtypes(include="number").columns.tolist()
selected = st.multiselect(
    "Select numeric columns for line chart", num_cols, default=num_cols[:1]
)
if selected:
    st.line_chart(df[selected])

###################################################
################### Correlation table
###################################################

st.subheader("Part 5: Correlation table")

st.dataframe(df.corr(numeric_only=True).round(2))

###################################################
################### Bonus 1: Sidebar for Controls
###################################################

st.sidebar.header("Bonus 1: Sidebar for Controls")

###################################################
################### Bonus 2: Text input to filter rows
###################################################

st.subheader("Bonus 2: Filter rows by text input")
st.sidebar.subheader("Bonus 2: Filter rows by text input")
col = st.sidebar.selectbox("Choose a column", df.columns, key="bonus_selectbox")
filter_value = st.sidebar.text_input("Enter numerical max threshold to display")


if filter_value:
    try:
        filter_value = float(filter_value)
        st.dataframe(df.loc[df[col] < filter_value, [col]])
    except Exception as e:
        st.warning(f"There is an error displaying your selection: {e}")
else:
    st.dataframe(df)


###################################################
################### Bonus 3: Collapsible Summary Statistics Section
###################################################

st.subheader("Bonus 3: Collapsible Summary Statistics Section")
with st.expander("Summary Statistics"):
    st.dataframe(df.describe())
