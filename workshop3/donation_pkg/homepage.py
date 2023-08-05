def show_homepage():
    while True:
        print("          === DonateMe Homepage ===          ")
        print("---------------------------------------------")
        print("| 1.    Login       | 2.    Register         |")
        print("---------------------------------------------")
        print("| 3.    Donate      | 4.    Show Donations   |")
        print("---------------------------------------------")
        print("|              5.    Exit                    |")
        print("---------------------------------------------")

        option = input("Choose an option:")
        if input == "1":
            account.show_balance(balance)
        elif input == "2":
            account.deposit(balance)
            print(f"Current Balance: ${float(balance)}")
        elif input == "3":
            account.withdraw(balance)
            print(f"Current Balance: ${float(balance)}")
        else:
            account.logout(name)
            break
