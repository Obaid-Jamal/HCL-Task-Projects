import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv("loan_data.csv")

# Clean column names
df.columns = df.columns.str.strip().str.lower()

# # Show columns (IMPORTANT - check once)
# st.write("Columns:", df.columns)

# Fill missing values
df.fillna(df.mean(numeric_only=True), inplace=True)

# ---- AUTO SELECT NUMERIC COLUMNS ----
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

# Use first 3 numeric columns as features
X = df[numeric_cols[:3]]

# Use last column as target
y = df[numeric_cols[-1]]

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# ---- UI ----
st.title("Loan Prediction (Random Forest)")

val1 = st.number_input("Annual Income", 0.0)
val2 = st.number_input("Credit Score", 0.0)
val3 = st.number_input("Loan Amount", 0.0)

if st.button("Predict"):
    prediction = model.predict([[val1, val2, val3]])

    if prediction[0] == 1:
        st.success("Loan Approved ✅")
    else:
        st.error("Loan Rejected ❌")
