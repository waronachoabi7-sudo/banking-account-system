account_number = int(input("Enter account number: "))
account_type = input("Enter account type ('c' for Cheque and 's' for Savings): ").lower()
current_balance = float(input("Enter current account balance: "))
minimum_balance = float(input("Enter minimum balance: "))

message = ""

if current_balance < minimum_balance:
    if account_type == 's':
        current_balance -= 10
        message = "Service charge fee of R10 (Savings Account is below minimum balance)"
    elif account_type == 'c':
        current_balance -= 25
        message = "Service charge fee of R25 (Cheque Account is below minimum balance)"
else:
    if account_type == 's':
        interest = current_balance * 0.04
        current_balance += interest
        message = "4% interest added to Savings Account"
    elif account_type == 'c':
        remainder = current_balance - minimum_balance
        if remainder <= 5000:
            interest = current_balance * 0.03
            current_balance += interest
            message = "3% interest added to Cheque Account (≤ 5000 above minimum)"
        else:
            interest = current_balance * 0.05
            current_balance += interest
            message = "5% interest added to Cheque Account (> 5000 above minimum)"


print("\n--- Account Summary ---")
print("Account number:", account_number)
print("Account type:", "Savings" if account_type == 's' else "Cheque")
print("New balance: R{:.2f}".format(current_balance))
print("Action taken:", message)
