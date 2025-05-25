from datetime import datetime

# ---- Transaction Class ----
class Transaction:
    def __init__(self, amount, type_, category, note=""):
        self.amount = amount
        self.type = type_
        self.category = category
        self.note = note
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M")

    def __str__(self):
        return f"[{self.date}] {self.type} - {self.category}: ${self.amount:.2f} | Note: {self.note}"


# ---- Budget Manager Class ----
class BudgetManager:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_total_income(self):
        return sum(t.amount for t in self.transactions if t.type == "Income")

    def get_total_expenses(self):
        return sum(t.amount for t in self.transactions if t.type == "Expense")

    def get_balance(self):
        return self.get_total_income() - self.get_total_expenses()

    def show_all_transactions(self):
        if not self.transactions:
            print("No transactions yet.")
            return
        for t in self.transactions:
            print(t)


# ---- Main Program (Console UI) ----
def main():
    manager = BudgetManager()

    while True:
        print("\n====== Personal Budget Tracker ======")
        print("1. Add Transaction")
        print("2. Show Summary")
        print("3. Show All Transactions")
        print("4. Exit")
        choice = input("Select an option (1-4): ")

        if choice == "1":
            try:
                amount = float(input("Enter amount: $"))
                type_ = input("Type (Income/Expense): ").capitalize()
                if type_ not in ["Income", "Expense"]:
                    print("Invalid type. Must be 'Income' or 'Expense'.")
                    continue
                category = input("Enter category (e.g. Food, Rent, Salary): ")
                note = input("Optional note: ")
                t = Transaction(amount, type_, category, note)
                manager.add_transaction(t)
                print("✅ Transaction added!")
            except ValueError:
                print("Invalid input. Amount must be a number.")
        
        elif choice == "2":
            print("\n====== Summary ======")
            print(f"Total Income:   ${manager.get_total_income():.2f}")
            print(f"Total Expenses: ${manager.get_total_expenses():.2f}")
            print(f"Current Balance: ${manager.get_balance():.2f}")

        elif choice == "3":
            print("\n====== Transaction History ======")
            manager.show_all_transactions()

        elif choice == "4":
            print("👋 Exiting... Thank you!")
            break

        else:
            print("Invalid choice. Please select 1-4.")

# Run the program
if __name__ == "__main__":
    main()
