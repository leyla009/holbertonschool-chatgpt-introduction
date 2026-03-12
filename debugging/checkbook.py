def main():
    cb = Checkbook()
    while True:
        action = input("\nWhat would you like to do? (deposit, withdraw, balance, exit): ").lower()
        
        if action == 'exit':
            break
        elif action in ['deposit', 'withdraw']:
            try:
                # Get the amount and attempt to convert it to a float
                amount = float(input(f"Enter the amount to {action}: $"))
                if amount < 0:
                    print("Please enter a positive amount.")
                    continue
                
                # Perform the requested action
                if action == 'deposit':
                    cb.deposit(amount)
                else:
                    cb.withdraw(amount)
            except ValueError:
                # This catches the error if the input isn't a valid number
                print("Invalid input. Please enter a valid numeric amount.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")
