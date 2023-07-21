import streamlit as st
import pandas as pd

# Create an empty dataframe to store expenses
expenses = pd.DataFrame(columns=['Date', 'Category', 'Amount'])

# Sidebar - Add expense
st.sidebar.header("Add New Expense")

date = st.sidebar.date_input("Date", value=pd.Timestamp.now())
category = st.sidebar.selectbox("Category", ['Food', 'Rent', 'Transportation', 'Other'])
amount = st.sidebar.number_input("Amount", value=0.0)

if st.sidebar.button("Add Expense"):
    new_expense = pd.DataFrame({'Date': [date], 'Category': [category], 'Amount': [amount]})
    expenses = pd.concat([expenses, new_expense], ignore_index=True)
    st.sidebar.success("Expense added successfully!")

# Main content
st.title("Personal Finance Tracker")

st.header("Expenses")
st.dataframe(expenses)

st.header("Summary")
total_expenses = expenses['Amount'].sum()
st.write("Total Expenses:", total_expenses)

# Visualize expenses by category
expenses_by_category = expenses.groupby('Category')['Amount'].sum()
st.bar_chart(expenses_by_category)

# Save expenses to Excel
if st.button("Save to Excel"):
    file_name = "expenses.xlsx"
    expenses.to_excel(file_name, index=False)
    st.success(f"Data saved to {file_name}")
