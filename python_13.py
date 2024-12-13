class Bank():
    acc_bal = 10000
    transaction_count = 0
    def deposit(self):
        if self.transaction_count >= 3:
            print("Transaction limit reached. You can only perform 3 deposits.")
            return
        amount = float(input("Enter the amount to deposit: "))
        if amount < 100:
            print("Deposit amount must be at least 100")
        elif amount > 50000:
            print("Deposit amount cannot exceed 50,000")
        elif amount % 100 != 0:
            print("deposit amount must be a multiple of 100")
        else:
            self.acc_bal += amount
            print(f"Successfully deposited {amount}. New balance: {self.acc_bal}")
    def withdraw(self):
        if self.transaction_count >= 3:
            print("Transaction limit reached. You can only perform 3 withdrawals.")
            return
        amount = float(input("Enter amount to withdraw: "))
        if amount < 100:
            print("Withdrawal amount must be at least 100")
        elif amount > 20000:
            print("Withdrawal amount cannot exceed 20,000")
        elif amount % 100 != 0:
            print("Withdrawal amount must be a multiple of 100")
        elif amount > (self.acc_bal - 500):
            print("You must maintain a minimum balance of 500")
        elif amount <= self.acc_bal:
            self.acc_bal -= amount
            self.transaction_count += 1
            print(f"Successfully withdrew {amount}. New balance: {self.acc_bal}")
        else:
            print("Insufficient balance.")
    def tot_balance(self):
        print(f"Your current balance is: {self.acc_bal}")
    def viewOptions(self):
        while True:
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Balance Enquiry")
            print("0. Exit")
            option = int(input("Choose option: "))
            if option == 1:
                self.deposit()
            elif option == 2:
                self.withdraw()
            elif option == 3:
                self.tot_balance()
            elif option == 0:
                print("Exiting")
                break
            else:
                print("Invalid option. Please choose again.")
    def validatepin(self):
        for i in range(3):
            pin = int(input("Enter your PIN: "))
            if pin == 1234:
                self.viewOptions()
                break
            else:
                if i < 2:
                    print("Invalid PIN number. Enter the pin again.")
                else:
                    print("Invalid pin, too many attempts.")
obj = Bank()
obj.validatepin()