import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simple Data Dashboard")

upload_file = st.file_uploader("Upload a CSV file", type=["csv"])

if upload_file is not None:
    # Read the CSV file
    df = pd.read_csv(upload_file)

    st.subheader("Data Preview:")
    st.write(df.head())

    st.write("Data Summary:")
    st.write(df.describe())

    st.subheader("Filter Data:")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select a column to filter", columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select a value to filter by", unique_values)

    filtered_df = df[df[selected_column] == selected_value]
    st.write("Filtered Data:")
    st.write(filtered_df)

    st.subheader("Plot Data:")
    x_column = st.selectbox("Select x-axis columns to plot", columns)
    y_column = st.selectbox("Select y-axis columns to plot", columns)

    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])

else:
    st.write("Please upload a CSV file to get started.")
        
