import matplotlib.pyplot as plt
from collections import defaultdict
from utils.io_utils import load_expenses
from datetime import datetime

def visualize_expenses():
    expenses = load_expenses()
    now = datetime.now()
    summary = defaultdict(float)

    for e in expenses:
        e_date = datetime.strptime(e['date'], '%Y-%m-%d')
        if e_date.month == now.month and e_date.year == now.year:
            summary[e['category']] += e['amount']

    if not summary:
        print("No data to visualize.")
        return

    categories = list(summary.keys())
    values = list(summary.values())

    plt.figure(figsize=(8, 5))
    plt.bar(categories, values, color='skyblue')
    plt.title("Expenses by Category (This Month)")
    plt.ylabel("Amount (₹)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
