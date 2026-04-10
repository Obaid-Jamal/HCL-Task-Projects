import streamlit as st
from salary_model import predict_salary
from loan_model import check_loan

st.title("ML Prediction App")

option = st.selectbox("Choose Task",
                      ["Salary Prediction", "Loan Eligibility"])

# Salary Prediction
if option == "Salary Prediction":
    exp = st.number_input("Enter Experience (years)", min_value=0.0)

    if st.button("Predict Salary"):
        salary = predict_salary(exp)
        st.success(f"Estimated Salary: ₹{salary:.2f}")

# Loan Prediction
elif option == "Loan Eligibility":
    income = st.number_input("Enter Income")
    credit = st.number_input("Enter Credit Score")

    if st.button("Check Eligibility"):
        result = check_loan(income, credit)

        if result == 1:
            st.success("Loan Approved ✅")
        else:
            st.error("Loan Not Approved ❌")