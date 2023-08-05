from donations_pkg.homepage import show_homepage, show_donations
from donations_pkg.user import login, register, donate


database = {"admin": "password123"}
donations = []
authorized_user = ""



while True:
    show_homepage()
    if authorized_user == "":
        print("You must be logged in to donate.")
    else:
        print(f"Logged in as: {authorized_user}")
    option = input("Choose an option:")
    if option == "1":
        username = input("Username:")
        password = input("Password:")
        authorized_user = login(database, username, password)
        if authorized_user == "":
            print("\nUser not found. Please register.")
    elif option == "2":
        print("Please register by filling out the following...\n")
        username = input("Username:")
        password = input("Password:")
        authorized_user = register(database, username)
        """
        if authorized_user != "":
            for i in database:
                i = username
                database[i] = password
        """
    elif option == "3":
        if authorized_user == "":
            print("You are not logged in")
        else:
            donation_string = donate(authorized_user)
            # needs to be fixed
            donations.append(donation_string)
            print(f"{donations}")
           
    elif option == "4":
        show_donations(donations)
    else:
        print("Goodbye!")
        break
        