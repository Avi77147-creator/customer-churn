import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Customer Churn Dashboard", layout="wide")

st.title("📊 Customer Churn Analysis Dashboard")

# File upload
uploaded_file = st.file_uploader("Upload your churn dataset (CSV file)", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.subheader("🔍 Dataset Preview")
    st.dataframe(df.head())

    st.subheader("📈 Dataset Overview")
    st.write("Shape of dataset:", df.shape)
    st.write(df.describe())

    # Select columns
    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    categorical_cols = df.select_dtypes(include='object').columns.tolist()

    # Plot Churn Distribution
    if "Churn" in df.columns:
        st.subheader("🚨 Churn Distribution")
        churn_counts = df["Churn"].value_counts()
        st.bar_chart(churn_counts)

    # Correlation heatmap
    if len(numeric_cols) >= 2:
        st.subheader("📊 Correlation Heatmap")
        fig, ax = plt.subplots()
        sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)

    # Filter by category (e.g., Gender or Department)
    if categorical_cols:
        st.subheader("📂 Filter by Category")
        col_to_filter = st.selectbox("Select a column to filter", categorical_cols)
        selected_value = st.selectbox(f"Select a value from {col_to_filter}", df[col_to_filter].unique())
        filtered_df = df[df[col_to_filter] == selected_value]
        st.dataframe(filtered_df)

else:
    st.info("Please upload a dataset to get started.")

