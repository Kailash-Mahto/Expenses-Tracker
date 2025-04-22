import json
from utils.io_utils import load_expenses
from datetime import datetime
from collections import defaultdict

def check_budget():
    try:
        with open('data/budget.json') as f:
            budget_data = json.load(f)
    except FileNotFoundError:
        print("No budget file found. Set your budget in data/budget.json.")
        return

    expenses = load_expenses()
    now = datetime.now()
    total_by_category = defaultdict(float)

    for e in expenses:
        e_date = datetime.strptime(e['date'], '%Y-%m-%d')
        if e_date.month == now.month and e_date.year == now.year:
            total_by_category[e['category']] += e['amount']

    print("\n--- Budget Check ---")
    for category, limit in budget_data.items():
        spent = total_by_category.get(category, 0)
        print(f"{category}: Spent ₹{spent:.2f} / ₹{limit:.2f}", end=' ')
        if spent > limit:
            print(", Over budget!")
        else:
            print(", Within budget")
