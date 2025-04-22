import csv
from datetime import datetime

def log_expense():
    date = input("Enter date (YYYY-MM-DD) or leave empty for today: ")
    if not date:
        date = datetime.now().strftime('%Y-%m-%d')
    category = input("Enter category (e.g. Food, Transport): ")
    amount = float(input("Enter amount: "))
    note = input("Optional note: ")

    with open('expenses.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, note])
    print("Expense logged successfully.")

def load_expenses():
    expenses = []
    try:
        with open('expenses.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                date, category, amount, note = row
                expenses.append({
                    'date': date,
                    'category': category,
                    'amount': float(amount),
                    'note': note
                })
    except FileNotFoundError:
        pass
    return expenses
