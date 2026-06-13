import json
from datetime import datetime

expense_file = 'expenses.json'
log_file = 'log.txt'

# Decorator
def log_call(func):
    def wrapper(*args, **kwargs):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(log_file, 'a') as log:
            log.write(f"{timestamp} | {func.__name__} | args={args} | kwargs={kwargs}\n")
        return func(*args, **kwargs)
    return wrapper

# Load expenses
def load_expense():
    try:
        with open(expense_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save expenses
def save_expense(expenses):
    with open(expense_file, 'w') as file:
        json.dump(expenses, file, indent=2)

# Add expense
@log_call
def add_expense(amount, category):
    expenses = load_expense()
    expense = {"Category": category, "Amount": amount}
    expenses.append(expense)
    save_expense(expenses)
    print("Expense added successfully!")

# Get summary
@log_call
def get_summary():
    expenses = load_expense()
    summary = {}                              
    for expense in expenses:
        category = expense["Category"]
        amount = expense["Amount"]
        summary[category] = summary.get(category, 0) + amount
    print("\nExpense Summary:")               
    for category, total in summary.items():
        print(f"{category}: ₹{total}")
    return summary                          
# View all expenses
@log_call
def view_all():
    expenses = load_expense()
    if not expenses:
        print("No expenses recorded.")
    else:
        print("\nAll Expenses:")
        for i, expense in enumerate(expenses, start=1):
            print(f"{i}. Category: {expense['Category']} | Amount: ₹{expense['Amount']}")

# Read logs
def read_logs():
    try:
        counts = {}
        with open(log_file, "r") as file:
            for line in file:
                parts = line.split("|")      
                if len(parts) >= 2:
                    func_name = parts[1].strip()
                    counts[func_name] = counts.get(func_name, 0) + 1
        print("\nFunction Call Counts:")
        for func, count in counts.items():
            print(f"{func}: {count} time(s)")
    except FileNotFoundError:
        print("No log file found.")

# Menu
while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Summary")
    print("3. View All Expenses")
    print("4. Read Logs")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))
        add_expense(amount, category)
    elif choice == "2":
        get_summary()
    elif choice == "3":
        view_all()
    elif choice == "4":
        read_logs()
    elif choice == "5":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")