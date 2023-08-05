from donations_pkg.homepage import show_homepage
from donations_pkg.user import login, register


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
        print("TODO: Write Donate Functionality")
    elif option == "4":
        print("TODO: Write Donations Functionality")
    else:
        print("Goodbye!")
        break
        