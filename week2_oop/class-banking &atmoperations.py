
#BANKING

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder   # public
        self.__balance = balance               # private

    def deposit(self, amount):                # public
        self.__balance += amount

    def withdraw(self, amount):               # public
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):                    # public
        return self.__balance


acc = BankAccount("Veera", 10000)

acc.deposit(2000)
print('after deposit - balance:')
print(acc.get_balance()) 
acc.withdraw(3000)
print('after withdraw - balance:')
print(acc.get_balance()) 

print(acc.get_balance())   # 9000

#ATM VALIDATION

class ATM:
    def __init__(self, pin, balance):
        self.__pin = pin
        self.__balance = balance

    def __validate_pin(self, pin):    # private
        return self.__pin == pin

    def withdraw(self, pin, amount):  # public
        if not self.__validate_pin(pin):
            return "Invalid PIN"

        if amount > self.__balance:
            return "Insufficient funds"

        self.__balance -= amount
        return f"Withdrawn ₹{amount}"
atm = ATM(1234, 5000)
print('ATM WITHDRAWAL')
print(atm.withdraw(1234, 2000))
print(atm._ATM__balance)
print(atm.withdraw(1111, 1000))

#realtime interactions
#BANKING OPERATIONS
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return "Withdrawal successful"
        return "Insufficient balance"

    def get_balance(self):
        return self.__balance
name = input("Enter account holder name: ")
balance = int(input("Enter opening balance: "))

acc = BankAccount(name, balance)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        amount = int(input("Enter deposit amount: "))
        acc.deposit(amount)
        print("Amount deposited")

    elif choice == "2":
        amount = int(input("Enter withdrawal amount: "))
        print(acc.withdraw(amount))

    elif choice == "3":
        print("Current Balance:", acc.get_balance())

    elif choice == "4":
        break

    else:
        print("Invalid choice")

#ATM OPERATIONS
class ATM:
    def __init__(self, pin, balance):
        self.__pin = pin
        self.__balance = balance

    def __validate_pin(self, pin):
        return self.__pin == pin

    def withdraw(self, pin, amount):
        if not self.__validate_pin(pin):
            return "Invalid PIN"
        if amount > self.__balance:
            return "Insufficient balance"
        self.__balance -= amount
        return f"Please collect ₹{amount}"

    def check_balance(self, pin):
        if not self.__validate_pin(pin):
            return "Invalid PIN"
        return f"Balance: ₹{self.__balance}"


pin = int(input("Set your ATM PIN: "))
balance = int(input("Enter initial balance: "))

atm = ATM(pin, balance)

while True:
    print("\n1. Withdraw")
    print("2. Check Balance")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        user_pin = int(input("Enter PIN: "))
        amount = int(input("Enter amount: "))
        print(atm.withdraw(user_pin, amount))

    elif choice == "2":
        user_pin = int(input("Enter PIN: "))
        print(atm.check_balance(user_pin))

    elif choice == "3":
        break

    else:
        print("Invalid option")

