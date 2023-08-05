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
        if option == "1":
            print("TODO: Write Login Functionality")
        elif option == "2":
            print("TODO: Write Register Functionality")
        elif option == "3":
            print("TODO: Write Donate Functionality")
        elif option == "4":
            print("TODO: Write Donations Functionality")
        else:
            print("Goodbye!")
            break
        
