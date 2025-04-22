from utils.io_utils import log_expense, load_expenses
from utils.report_utils import generate_summary
from utils.budget_utils import check_budget
from utils.visualization import visualize_expenses

def main():
    while True:
        print("\n=== Expense Tracker Menu ===")
        print("1. Log new expense")
        print("2. Show weekly/monthly summary")
        print("3. Visualize expenses")
        print("4. Check budget & overages")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            log_expense()
        elif choice == '2':
            generate_summary()
        elif choice == '3':
            visualize_expenses()
        elif choice == '4':
            check_budget()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()
