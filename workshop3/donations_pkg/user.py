

def login(database = {}, username = "", password = ""):
    for i in database:
        if i == username and database[i] == password:
            print(f"Welcome {username}!!!")
        elif i == username and database[i] != password:
            return ""
        else:
            print("User not in the database")
            return ""