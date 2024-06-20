import json
import matplotlib.pyplot as plt

# Variables to store financial data
income = 0.0
expenses = 0.0
savings = 0.0
transactions = []
categorized_expenses = {}

# Function to display the welcome message
def welcome_message():
    print("Welcome to the Personal Finance Tracker!")
    print("You can use this program to track your income, expenses, and savings.")
    print("Follow the instructions to input your financial data and generate reports.")

# Function to add income
def get_income():
    global income
    try:
        amount = float(input("Enter the amount of income: "))
        income += amount
        transactions.append({'type': 'income', 'amount': amount})
    except ValueError:
        print("Invalid input! Please enter a valid number.")

# Function to add expense
def get_expense():
    global expenses
    try:
        amount = float(input("Enter the amount of expense: "))
        category = input("Enter the category of the expense: ")
        expenses += amount
        transactions.append({'type': 'expense', 'amount': amount, 'category': category})
        
        if category in categorized_expenses:
            categorized_expenses[category] += amount
        else:
            categorized_expenses[category] = amount
    except ValueError:
        print("Invalid input! Please enter a valid number.")

# Function to display financial summary
def display_data():
    global savings
    savings = income - expenses
    print("\nCurrent Financial Summary:")
    print(f"Total Income: ${income:.2f}")
    print(f"Total Expenses: ${expenses:.2f}")
    print(f"Total Savings: ${savings:.2f}")

# Function to display categorized expenses
def display_categorized_expenses():
    print("\nCategorized Expenses:")
    for category, amount in categorized_expenses.items():
        print(f"{category}: ${amount:.2f}")

# Function to plot expenses by category
def plot_expenses():
    categories = list(categorized_expenses.keys())
    amounts = list(categorized_expenses.values())

    plt.figure(figsize=(10, 5))
    plt.bar(categories, amounts, color='skyblue')
    plt.xlabel('Categories')
    plt.ylabel('Amount ($)')
    plt.title('Expenses by Category')
    plt.show()

# Function to save transactions to a file
def save_transactions():
    with open('transactions.json', 'w') as file:
        json.dump(transactions, file)
    print("Transactions saved successfully!")

# Function to load transactions from a file
def load_transactions():
    global income, expenses
    try:
        with open('transactions.json', 'r') as file:
            data = json.load(file)
            for transaction in data:
                transactions.append(transaction)
                if transaction['type'] == 'income':
                    income += transaction['amount']
                elif transaction['type'] == 'expense':
                    expenses += transaction['amount']
                    category = transaction['category']
                    if category in categorized_expenses:
                        categorized_expenses[category] += transaction['amount']
                    else:
                        categorized_expenses[category] = transaction['amount']
    except FileNotFoundError:
        print("No previous transaction data found.")

# Function to display the main menu and handle user choices
def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Display Financial Summary")
        print("4. Display Categorized Expenses")
        print("5. Plot Expenses by Category")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            get_income()
        elif choice == '2':
            get_expense()
        elif choice == '3':
            display_data()
        elif choice == '4':
            display_categorized_expenses()
        elif choice == '5':
            plot_expenses()
        elif choice == '6':
            print("Thank you for using the Personal Finance Tracker. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")

# Main program execution
welcome_message()
load_transactions()
main_menu()
save_transactions()
