import math

def login(database = {}, username = "", password = ""):
    for i in database:
        if i == username and database[i] == password:
            print(f"Welcome back {username}!!!")
        elif i == username and database[i] != password:
            return ""
        else:
            print("User not in the database")
            return ""
        
def register(database, username):
    for i in database:
        if i == username:
            print("Username already registered")
            return ""
        else:
            print(f"{username} has been registered.")
            return username
        


