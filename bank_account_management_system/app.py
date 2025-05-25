class BankAccount:
    def __init__(self, name, acc_no, balance=0):
        self.name = name
        self.acc_no = acc_no
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"\n✅ {amount} deposited successfully.")
        else:
            print("\n❌ Invalid amount. Please enter a positive number.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"\n✅ {amount} withdrawn successfully.")
        else:
            print("\n❌ Insufficient balance or invalid amount.")

    def check_balance(self):
        print(f"\n💰 Current balance: {self.__balance}")

    def display_details(self):
        print("\n📄 Account Details:")
        print(f"👤 Account Holder: {self.name}")
        print(f"🏦 Account Number: {self.acc_no}")


def main():
    print("=======================================")
    print("💳 Welcome to the Bank Account System 💳")
    print("=======================================")

    name = input("👤 Enter account holder name: ")
    acc_no = input("🔢 Enter account number: ")
    account = BankAccount(name, acc_no)

    while True:
        print("\n---------- MENU ----------")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. View Account Details")
        print("5. Exit")
        print("--------------------------")

        choice = input("📥 Enter your choice (1-5): ")

        if choice == '1':
            try:
                amount = float(input("💵 Enter amount to deposit: "))
                account.deposit(amount)
            except ValueError:
                print("❌ Please enter a valid number.")

        elif choice == '2':
            try:
                amount = float(input("💵 Enter amount to withdraw: "))
                account.withdraw(amount)
            except ValueError:
                print("❌ Please enter a valid number.")

        elif choice == '3':
            account.check_balance()

        elif choice == '4':
            account.display_details()

        elif choice == '5':
            print("\n👋 Thank you for using the Bank Account System. Goodbye!")
            break

        else:
            print("❌ Invalid choice! Please select from 1 to 5.")


if __name__ == "__main__":
    main()
