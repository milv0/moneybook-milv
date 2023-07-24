import streamlit as st
import pandas as pd

# Create an empty dataframe to store expenses
expenses = pd.DataFrame(columns=['Date', 'Category', 'Amount'])

# Sidebar - Add expense
st.sidebar.header("입력란")

date = st.sidebar.date_input("Date", value=pd.Timestamp.now())
category = st.sidebar.selectbox("Category", ['식비', '교통비', '경조사비', '병원'])
amount = st.sidebar.number_input("Amount", value=0.0)

if st.sidebar.button("Add Expense"):
    new_expense = pd.DataFrame({'Date': [date], 'Category': [category], 'Amount': [amount]})
    expenses = pd.concat([expenses, new_expense], ignore_index=True)
    st.sidebar.success("Expense added successfully!")

# Main content
st.title("가계부")

st.header("내역")
st.dataframe(expenses)

st.header("Summary")
total_expenses = expenses['Amount'].sum()
st.write("Total Expenses:", total_expenses)

# Visualize expenses by category
expenses_by_category = expenses.groupby('Category')['Amount'].sum()
st.bar_chart(expenses_by_category)

# Save expenses to Excel
if st.button("Save to Excel"):
    file_name = "moneybook.csv"
    expenses.to_excel(file_name, index=False)
    st.success(f"Data saved to {file_name}")
