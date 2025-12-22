import json
import os
userfile = "user.json"
productfile = "product.json"
def initializeFile():
    if not os.path.exists(userfile):
        with open(userfile, "w") as file:
            json.dump([], file)
    if not os.path.exists(productfile):
        with open(productfile, "w") as file:
            json.dump([], file)
       

def load_users():
    with open(userfile, "r") as file:
        return json.load(file)

def load_products():
    with open(productfile, "r") as file:
        return json.load(file)


def save_users(users):
    with open(userfile, "w") as file:
        json.dump(users, file, indent=4)


def save_product(products):
    with open(productfile, "w") as file:
        json.dump(products, file, indent=4)

def showAllProducts():
    print("Showing all products...")

def showAllUsers():
    print("Showing all users...")

def deleteProduct(*args):
    print("Deleting product...")

def deleteUser(username):
    print(f"Deleting user {username}...")

def Logout(user):
    print(f"{user['name']} logged out.")

def showAllSellerProducts():
    print("Showing seller products...")

def addProduct(user):
    print("Adding product...")

def addToCart(pid, user):
    print("Added product to cart.")

def removeFromCart(pid, user):
    print("Removed product from cart.")

def showCart(user):
    print("Showing cart...")


def adminDashboard(user):
    print(f"Welcome {user['name']} in MH-Mall as a {user['role']} ......... Enter!!!!") 
    print("1 for Show all products")  
    print("2 for update Profile")
    print("3 for all users")
    print("4 for delete product")
    print("5 for delete user")
    print("6 for Logout")

    choice = input("Enter Choice: \t")

    if choice == "1":
        showAllProducts()
    elif choice == "2" :
        updateProfile(user)
    elif choice == "3" :
        showAllUsers()
    elif choice == "4" :
        id = int(input("Enter the id of product...."))
        deleteProduct(id) 
    elif choice == "5" :
        username = input("enter the username of user")
        deleteUser(username)     
    elif choice == "6":
        Logout(user)
    else :
        print("invalid Input")    


def sellerDashboard(user):
    print(f"Welcome {user['name']} in MH-Mall as a {user['role']} ......... Enter!!!!") 
    print("1 for Show all my products")  
    print("2 for update Profile")
    print("3 for delete product")
    print("4 for Logout")
    print("5 for adding a product")

    choice = input("Enter Choice: \t")

    if choice == "1":
        showAllSellerProducts()
    elif choice == "2" :
        updateProfile(user)
    elif choice == "3" :
        id = int(input("Enter the id of product...."))
        deleteProduct(id , user) 
    elif choice == "5" :
        addProduct(user)     
    elif choice == "4":
        Logout(user)
    else :
        print("invalid Input")

def customerDashboard(user):
    print(f"Welcome {user['name']} in MH-Mall as a {user['role']} ......... Enter!!!!") 
    print("1 for Show all products")  
    print("2 for update Profile")
    print("4 for Logout")
    print("3 for adding to cart")
    print("5 for Removing from cart")
    print("6 for to show all cart options")

    choice = input("Enter Choice: \t")

    if choice == "1":
        showAllProducts()
    elif choice == "2" :
        updateProfile(user)
    elif choice == "3" :
        id = int(input("Enter the id of product...."))
        addToCart(id , user)    
    elif choice == "4":
        Logout(user)
    elif choice == "5" :
        id = int(input("Enter the id of product...."))
        removeFromCart(id , user)    
    elif choice == "6" :
        showCart(user)    
    else :
        print("invalid Input")

def updateProfile(user):    
   print(user)

def signIn():
    email = input("Enter your email !!!!\t").strip()
    password = input("Enter your password !!!!\t").strip()

    users = load_users()
    
    for user in users :
        print(user)
        if user["email"] == email and user["password"] == password :
            print("Login successfully")
            if user["role"] == "admin" :
                adminDashboard(user)
            elif user["role"] == "seller" :
                sellerDashboard(user)
            else :
                customerDashboard(user)        
            return
        
    print("Login faild. Please try again")
    


def signUp():
    name = input("Enter your name !!!!\t")
    email = input("Enter your email !!!!\t")
    username = input("Enter your username !!!!\t")
    password = input("Enter your password !!!!\t")
    age = int(input("Enter your age !!!!\t"))
    gender = input("Enter your gender !!!!\t")
    address = input("Enter your address !!!!\t")
    phone = input("Enter your phone !!!!\t")
    print("enter your role \n \t admin \n \t seller \n \t customer")
    role = input("Enter your role !!!!\t")
    while role not in ["admin" , "seller" ,"customer"]:
        print("Invalid role.Enter again")
        role = input("Enter your role !!!!\t")

    new_user = {
        "name" : name,
        "email" : email,
        "username" : username ,
        "password" : password ,
        "age" : age,
        "gender": gender,
        "address" : address,
        "phone" : phone,
        "role" : role,
        "cart" : [],
    }    
    users = load_users()

    for user in users:
        if user["username"] == username :
            print("username alredy exists.")
            return
        elif user["email"] == email:
            print("email already exists.")
            return
        
    users.append(new_user)

    save_users(users)   
    print("Your account is registered successfully!! Now please sign in to use the account!!!!!")


def mainMenu():
    initializeFile()

    while True:
        print("\nWelcome to MH-Mall (Your destination for everything...)")
        print("Select an option:")
        print("1. Sign In")
        print("2. Sign Up")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            signIn()

        elif choice == "2":
            signUp()

        elif choice == "3":
            print("Thanks for using MH-Mall. Hope to see you again!")
            break

        else:
            print("Invalid choice. Please try again.")


mainMenu()
