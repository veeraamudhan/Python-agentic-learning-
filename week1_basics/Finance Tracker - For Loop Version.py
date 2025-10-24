# Finance Tracker - For Loop Version

balance = 0
transactions = []

# Ask how many transactions
n = int(input("How many transactions do you want to record? "))

for i in range(n):
    action = input(f"Transaction {i+1} - Enter 'deposit' or 'withdraw': ").lower()

    if action == "deposit":
        amount = float(input("Enter deposit amount: "))
        balance += amount
        transactions.append(f"Deposited: {amount}")
    elif action == "withdraw":
        amount = float(input("Enter withdrawal amount: "))
        if amount > balance:
            print("⚠️ Insufficient Balance! Transaction canceled.")
            transactions.append(f"Failed Withdrawal: {amount} (Insufficient funds)")
        else:
            balance -= amount
            transactions.append(f"Withdrew: {amount}")
    else:
        print("Invalid option. Skipped this transaction.")
        transactions.append("Invalid transaction entered")

# Summary
summary = "\n".join(transactions)
final_report = f"""
---- Finance Report ----
Transactions:
{summary}

Final Balance: {balance}
------------------------
"""

print(final_report)

# Save to file
with open("finance_report.txt", "w") as file:
    file.write(final_report)

print("✅ Report saved to finance_report.txt")
