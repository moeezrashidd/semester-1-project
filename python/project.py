import json
import os
import uuid

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


def saveUpdatedUser(user):
    users = load_users()

    for i, u in enumerate(users):
        if u["username"] == user["username"]:
            users[i] = user
            break

    save_users(users)


def showAllProducts(): 
    products = load_products()
    print( "\n " ,products)

def showAllUsers():
    users = load_users()
    print( "\n " ,users)

def deleteProduct():
    products = load_products()

    while True:
        try:
            prod_id = int(input("Enter the product ID to delete: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    for i, product in enumerate(products):
        if product["id"] == prod_id:
            del products[i]
            save_product(products)
            print("Product deleted successfully!")
            return True

    print("Product not found!")
    return False
 

     

def deleteUser():
    users = load_users()
    username = input("Enter the username to delete: ")

    user_found = False
    
    for i in range(len(users)):
        if users[i]["username"] == username:

            del users[i]
            user_found = True
            
            
            save_users(users)
            
            print(f"User '{username}' deleted successfully!")
            return True
    
    if not user_found:
        print("User not found!")
        retry = input("Would you like to try again? (yes/no): ")
        if retry.lower() == "yes":
            deleteUser()
        return False  



def addProduct(user):

    while True:
            try:
                price = int(input("Enter product price: "))
                if price <= 0:
                    print("Price must be a positive number!")
                    continue
                break
            except:
                print("Please enter a valid number!")

    title = input("Enter the title of your product: ")
    brand = input("Enter product brand: ")
    desc = input("Enter product description: ")
    sellerName = user["username"]
    

    product_id = int(str(uuid.uuid4().int)[:4])
    
    new_product = {
        "id": product_id, 
        "title": title,
        "price": price,
        "brand": brand,
        "desc": desc,
        "sellerName": sellerName
    }
    
    products = load_products()
    products.append(new_product)
    save_product(products)  
    
    print(f"Product added successfully! Product ID: {product_id}")



def addToCart(user):
    products = load_products()
    users = load_users()
    while True:
        try:
            prod_id = int(input("Enter the id of product to add in cart: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        for product in products:
            if product["id"] == prod_id:
                user["cart"].append(product)
                print(user)
                for i, u in enumerate(users):
                    if u["username"] == user["username"]:
                        users[i] = user
                        break
                save_users(users)
                print("Product added to cart successfully.")
                return  
        print("Product not found. Try another ID.")


def removeFromCart(user):
    products = load_products()
    users = load_users()
    while True:
        try:
            prod_id = int(input("Enter the id of product to add in cart: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        for product in products:
            if product["id"] == prod_id:
                user["cart"].remove(product)
                print(user)
                for i, u in enumerate(users):
                    if u["username"] == user["username"]:
                        users[i] = user
                        break
                save_users(users)
                print("Product added to cart successfully.")
                return  
        print("Product not found. Try another ID.")



def showCart(user):
    if len(user["cart"]) > 0:
        print(user["cart"])
    else:
        print("Empty cart.Please add products to cart.||||") 
           

def updateProfile(user):
    print("\n--- Update Profile (press Enter to skip) ---")

    name = input(f"Name [{user['name']}]: ").strip()
    if name:
        user["name"] = name

    email = input(f"Email [{user['email']}]: ").strip()
    if email:
        user["email"] = email

    password = input("Password [hidden]: ").strip()
    if password:
        user["password"] = password

    while True:
        age = input(f"Age [{user['age']}]: ").strip()
        if not age:
            break
        if age.isdigit():
            user["age"] = int(age)
            break
        print("Age must be a number.")

    gender = input(f"Gender [{user['gender']}]: ").strip()
    if gender:
        user["gender"] = gender

    address = input(f"Address [{user['address']}]: ").strip()
    if address:
        user["address"] = address

    phone = input(f"Phone [{user['phone']}]: ").strip()
    if phone:
        user["phone"] = phone

    print("\nProfile updated successfully.")
    saveUpdatedUser(user)
  
      


def Logout(user):
    print(f"{user['name']} logged out.")


def showAllSellerProducts(seller):
    products = load_products()
    sellerProducts = []
    for product in products:
        if product["seller"] == seller:
            sellerProducts.append(product)

    if len(sellerProducts) <= 0:
        print("No product is present|||||Enter product...")
    else:
        print(sellerProducts)    
        

def deleteAccount(user):
    users = load_users()

    for i in users:
        if i["username"] == user["username"]:
            users.remove(i)
            break

    save_users(users)    

def deleteUserProduct(user):
    
    showAllSellerProducts(user["username"])

  
    while True:
        try:
            prod_id = int(input("Enter the ID of the product to delete: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    
    products = user.get("cart", [])  
    for product in products:
        if product["id"] == prod_id:
            user["cart"].remove(product)
            print(f"Product with ID {prod_id} removed successfully from cart.")
            
            
            users = load_users()
            for i, u in enumerate(users):
                if u["username"] == user["username"]:
                    users[i] = user
                    break
            save_users(users)
            return

    print(f"No product with ID {prod_id} found in your cart.")
  



def adminDashboard(user):
    while True:
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
                deleteProduct() 
            elif choice == "5" :
                username = input("enter the username of user")
                deleteUser(username)     
            elif choice == "6":
                Logout(user)
                break
            else :
                print("invalid Input")    


def sellerDashboard(user):
    while True :
        print(f"Welcome {user['name']} in MH-Mall as a {user['role']} ......... Enter!!!!") 
        print("1 for Show all my products")  
        print("2 for update Profile")
        print("3 for delete product")
        print("4 for Logout")
        print("5 for adding a product")
        print("6 for deleting a account")


        choice = input("Enter Choice: \t")

        if choice == "1":
            showAllSellerProducts(user["username"])
        elif choice == "2" :
            updateProfile(user)
        elif choice == "3" :
            deleteUserProduct(user) 
        elif choice == "4":
            Logout(user)
            break
        elif choice == "5" :
            addProduct(user)     
        elif choice == "6" :
            deleteAccount(user)     
        else :
            print("invalid Input")

def customerDashboard(user):
    while True:
        print(f"Welcome {user['name']} in MH-Mall as a {user['role']} ......... Enter!!!!") 
        print("1 for Show all products")  
        print("2 for update Profile")
        print("3 for adding to cart")
        print("4 for Logout")
        print("5 for Removing from cart")
        print("6 to show all cart products")
        print("7 to delete account")

        choice = input("Enter Choice: \t")

        if choice == "1":
            showAllProducts()
        elif choice == "2" :
            updateProfile(user)
        elif choice == "3" :
            addToCart(user)    
        elif choice == "4":
            Logout(user)
            break
        elif choice == "5" :
            removeFromCart(user)    
        elif choice == "6" :
            showCart(user)    
        elif choice == "7" :
            deleteAccount(user)    
        else :
            print("invalid Input")



def signIn():
    email = input("Enter your email !!!!\t").strip()
    password = input("Enter your password !!!!\t").strip()

    users = load_users()
    
    for user in users :
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
    users = load_users()

    
    while True:
        name = input("Enter your name: ").strip()
        if name.isalpha() and len(name) > 3:
            break
        print("Name must be alphabetic and greater than 3 characters.")
    while True:
        username = input("Enter your username: ").strip()
        if len(username) <= 3:
            print("Username must be greater than 3 characters.")
            continue

        for u in users:
            if u["username"] == username:
                print("Username already exists. Enter another.")
                break  
        else:
            break

    while True:
        email = input("Enter your email: ").strip()
        if "@" in email and ".com" in email:
        
            for u in users:
                if u["email"] == email:
                    print("Email already exists. Enter another.")
                    break  
            else:
                
                break
        else:
            print("Enter a valid email ")

 
    while True:
        password = input("Enter your password: ").strip()
        if len(password) >= 6:
            break
        print("Password must be at least 6 characters.")


    while True:
        age = input("Enter your age: ").strip()
        if age.isdigit() and 10 <= int(age) <= 120:
            age = int(age)
            break
        print("Age must be a number between 10 and 120.")


    while True:
        gender = input("Enter your gender (M/F/Other): ").strip().lower()
        if gender in ["m", "f", "male", "female", "other"]:
            break
        print("Invalid gender. Enter M, F, or Other.")

    while True:
        address = input("Enter your address: ").strip()
        if address:
            break
        print("Address cannot be empty.")

 
    while True:
        phone = input("Enter your phone number: ").strip()
        if phone.isdigit() and 10 <= len(phone) <= 15:
            break
        print("Phone must be digits only (10-15 digits).")


    while True:
        print("Enter your role:\n\tadmin\n\tseller\n\tcustomer")
        role = input("Enter your role: ").strip().lower()
        if role in ["admin", "seller", "customer"]:
            break
        print("Invalid role. Enter again.")

    new_user = {
        "name": name,
        "email": email,
        "username": username,
        "password": password,
        "age": age,
        "gender": gender,
        "address": address,
        "phone": phone,
        "role": role,
        "cart": [],
    }

    users.append(new_user)
    save_users(users)
    print("Your account is registered successfully! Please sign in to use the account.")

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
