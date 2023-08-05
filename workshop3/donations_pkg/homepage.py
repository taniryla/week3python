

def show_homepage():
    print("          === DonateMe Homepage ===          ")
    print("---------------------------------------------")
    print("| 1.    Login       | 2.    Register         |")
    print("---------------------------------------------")
    print("| 3.    Donate      | 4.    Show Donations   |")
    print("---------------------------------------------")
    print("|              5.    Exit                    |")
    print("---------------------------------------------")

def donate(username):
    try:
        donation_amt = float(input("Enter amount to donate: "))
        # donation_amt = round(donation_amt, 2)
    except ValueError:
        print("Can't convert this...")
    donation_string = f"{username} has donated ${donation_amt:,.2f}"
    print("Thank you for your donation!!")
    return [donation_string, donation_amt]

def show_donations(donations):
    print("\n--- All Donations ---")
    if len(donations) == 0:
        print("Currently, there are no donations")
    else:
        total = 0
        for i in donations:
            print(i[0])
            total += i[1]
        print(f"Total: ${total:,.2f}\n")        