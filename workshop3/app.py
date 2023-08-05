from donations_pkg.homepage import show_homepage, show_donations, donate
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
        username = input("\nUsername:")
        password = input("Password:")
        authorized_user = login(database, username, password)
        if authorized_user == "":
            print("\nUser not found. Please register.")
    elif option == "2":
        print("Please register by filling out the following...\n")
        username = input("\nUsername:")
        password = input("Password:")
        authorized_user = register(database, username)
    
        if authorized_user != "":
           database[authorized_user] = password
    elif option == "3":
        if authorized_user == "":
            print("You are not logged in")
        else:
            donation_string = donate(authorized_user)
            donations.append(donation_string)
    elif option == "4":
        show_donations(donations)
    else:
        print("Goodbye!")
        break
        