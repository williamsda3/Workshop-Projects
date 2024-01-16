balance = 500
password = 123

# A single User's information
user = {
    'username': "N/A",
    'password': "N/A",
    'balance': 0
}

# Array to store all User's information
Users = []
Users.append(user)

# Functions for account actions
def show_balance():
    print("Current balance:", user["balance"])

def deposit(depositAmount):
    user["balance"] += depositAmount
    return user["balance"]

def withdraw(withdrawalAmount):
    if user["balance"] >= withdrawalAmount:
        user["balance"] -= withdrawalAmount
        return user["balance"]
    else:
        print("Insufficient funds.")
        return user["balance"]

#  Functions for User Auth
def signUp():
        username = input("Please enter a username \n >>")
        for user in Users:
                if username == user["username"] : # If the username is in the database, check for password match   
                       print("Username already taken: ", user["username"])
                       signUp()
                       return
        password = input("Please enter a password \n >>")
        
        user["username"] = username
        user["password"] = password
        Users.append(user)
        
def userLogin():
    
    # Get username from user
        username = input("Please enter a username \n >>")
        for user in Users:
                if username == user["username"] : # If the username is in the database, check for password match   
                        password = input("Please enter a password \n >>")
                        if password == user["password"] :
                            menu()
                            return
                        else:
                            print("Invalid Password")
                            userLogin()
                            break
                print("Username not found")
                userLogin()
    
        
        

# Menu for Account Interactions
def menu():
    while True :
        menu = input("Please select an option: \n1: view balance \n2: deposit \n3: withdraw \n0: exit\n")
        if menu == '1':
            show_balance()
        elif menu == '2':
            depositAmount = int(input("How much money would you like to deposit? "))
            deposit(depositAmount)
            show_balance()
        elif menu == '3':
            withdrawalAmount = int(input("How much would you like to withdraw? "))
            verification = input("Please input your account password:\n")
            if verification == user["password"]:
                withdraw(withdrawalAmount)
                show_balance()
            else:
                print("Incorrect password.")
        elif menu == '0':
            return
            
            
# Main Method
if __name__ == "__main__":
    signUp()
    print(Users)
    userLogin()