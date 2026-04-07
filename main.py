import pandas as pd
import matplotlib.pyplot as plt

# Load Data
try:
    df = pd.read_csv("data/expenses.csv")
    print("Data Loaded Successfully")
except Exception as e:
    print("Error loading file:", e)

# Data Cleaning
df.dropna(inplace=True)

# Basic Analysis
total_expense = df["Amount"].sum()
category_expense = df.groupby("Category")["Amount"].sum()

print("\nTotal Expense:", total_expense)
print("\nCategory-wise Expense:\n", category_expense)

# Bar Chart
plt.figure()
category_expense.plot(kind='bar')
plt.title("Expense by Category")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.savefig("visualizations/bar_chart.png")

# Pie Chart
plt.figure()
category_expense.plot(kind='pie', autopct='%1.1f%%')
plt.title("Expense Distribution")
plt.ylabel("")
plt.savefig("visualizations/pie_chart.png")

# Line Chart (Daily Expense Trend)
daily_expense = df.groupby("Date")["Amount"].sum()

plt.figure()
daily_expense.plot(kind='line', marker='o')
plt.title("Daily Expense Trend")
plt.xlabel("Date")
plt.ylabel("Amount")
plt.xticks(rotation=45)
plt.savefig("visualizations/line_chart.png")

plt.show()