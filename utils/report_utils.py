from collections import defaultdict
from datetime import datetime
from utils.io_utils import load_expenses
import csv

def generate_summary():
    expenses = load_expenses()
    choice = input("Generate summary for (w)eekly or (m)onthly? ").lower()
    now = datetime.now()
    summary = defaultdict(float)

    for e in expenses:
        e_date = datetime.strptime(e['date'], '%Y-%m-%d')
        if (choice == 'w' and e_date.isocalendar()[1] == now.isocalendar()[1]) or \
           (choice == 'm' and e_date.month == now.month and e_date.year == now.year):
            summary[e['category']] += e['amount']

    print("\n--- Summary ---")
    for category, total in summary.items():
        print(f"{category}: ₹{total:.2f}")

    export = input("Export this summary as CSV? (y/n): ").lower()
    if export == 'y':
        filename = f"{choice}_summary_{now.strftime('%Y%m%d')}.csv"
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Category', 'Total'])
            for k, v in summary.items():
                writer.writerow([k, v])
        print(f"Summary exported to {filename}")
