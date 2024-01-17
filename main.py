import bank

def main():
    acc_name = bank.BankAccount(input("What is your account name? > "))
    while True:
        try:
            match input(f"Choose an option for {acc_name.account_holder}\n[1] Withdraw\n[2] Deposit\n[3] Check balance\n >>> "):
                case "1":
                    acc_name.withdraw(float(input("Enter withdraw amount > ")))
                case "2":
                    acc_name.deposit(float(input("Enter deposit amount > ")))
                case "3":
                    print(f"Your balance is ${acc_name.balance:.2f}")
        except ValueError:
            print("Incorrect Input!")


if __name__ == "__main__":
    main()
