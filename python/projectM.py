
import json
import os

USER_FILE = "user.json"
PRODUCT_FILE = "product.json"

def initializeFiles():
    if not os.path.exists(USER_FILE):
        with open(USER_FILE, "w") as file:
            json.dump([], file)
    if not os.path.exists(PRODUCT_FILE):
        with open(PRODUCT_FILE, "w") as file:
            json.dump([], file)

def load_users():
    try:
        with open(USER_FILE, "r") as file:
            return json.load(file)
    except:
        return []

def save_users(users):
    with open(USER_FILE, "w") as file:
        json.dump(users, file, indent=4)

def load_products():
    try:
        with open(PRODUCT_FILE, "r") as file:
            return json.load(file)
    except:
        return []

def save_products(products):
    with open(PRODUCT_FILE, "w") as file:
        json.dump(products, file, indent=4)

def get_next_product_id():
    products = load_products()
    if not products:
        return 1
    max_id = max(int(p["id"]) for p in products)
    return max_id + 1

def showAllProducts():
    products = load_products()
    if not products:
        print("No products available.")
        return
    print("\n--- All Products ---")
    for product in products:
        print(f"ID: {product['id']}")
        print(f"Name: {product['name']}")
        print(f"Category: {product['category']}")
        print(f"Price: ${product['price']:.2f}")
        print(f"Stock: {product['stock']}")
        print(f"Seller: {product['seller_username']}")
        print("-" * 30)

def showAllUsers():
    users = load_users()
    if not users:
        print("No users found.")
        return
    print("\n--- All Users ---")
    for user in users:
        print(f"Username: {user['username']}")
        print(f"Name: {user['name']}")
        print(f"Email: {user['email']}")
        print(f"Role: {user['role']}")
        print(f"Phone: {user['phone']}")
        print("-" * 30)

def deleteProduct(product_id, current_user=None):
    products = load_products()
    found = False
    
    for product in products:
        if int(product["id"]) == product_id:
            if current_user and current_user["role"] == "seller":
                if product["seller_username"] != current_user["username"]:
                    print("You can only delete your own products.")
                    return
            found = True
            confirm = input(f"Delete product '{product['name']}'? (yes/no): ").lower()
            if confirm == "yes":
                products = [p for p in products if int(p["id"]) != product_id]
                save_products(products)
                print("Product deleted.")
            else:
                print("Deletion cancelled.")
            return
    
    if not found:
        print("Product not found.")

def deleteUser(username):
    users = load_users()
    user_exists = any(user['username'] == username for user in users)
    
    if not user_exists:
        print(f"User '{username}' not found.")
        return
    
    confirm = input(f"Delete user '{username}'? (yes/no): ").lower()
    if confirm != "yes":
        print("Deletion cancelled.")
        return
    
    users = [user for user in users if user['username'] != username]
    
    products = load_products()
    products = [p for p in products if p.get('seller_username') != username]
    
    save_users(users)
    save_products(products)
    print(f"User '{username}' deleted.")

def logout(user):
    print(f"{user['name']} logged out.")

def showAllSellerProducts(user):
    products = load_products()
    seller_products = [p for p in products if p["seller_username"] == user["username"]]
    
    if not seller_products:
        print("You have no products.")
        return
    
    print(f"\n--- Your Products ---")
    for product in seller_products:
        print(f"ID: {product['id']}")
        print(f"Name: {product['name']}")
        print(f"Category: {product['category']}")
        print(f"Price: ${product['price']:.2f}")
        print(f"Stock: {product['stock']}")
        print("-" * 30)

def addProduct(user):
    print("\n--- Add New Product ---")
    
    name = input("Product name: ").strip()
    if not name:
        print("Product name required.")
        return
    
    category = input("Category: ").strip()
    
    try:
        price = float(input("Price: "))
        if price <= 0:
            print("Price must be positive.")
            return
    except:
        print("Invalid price.")
        return
    
    try:
        stock = int(input("Stock quantity: "))
        if stock < 0:
            print("Stock cannot be negative.")
            return
    except:
        print("Invalid stock quantity.")
        return
    
    description = input("Description (optional): ").strip()
    
    products = load_products()
    
    new_product = {
        "id": get_next_product_id(),
        "name": name,
        "category": category,
        "price": price,
        "stock": stock,
        "description": description,
        "seller_username": user["username"],
        "seller_name": user["name"]
    }
    
    products.append(new_product)
    save_products(products)
    print(f"Product '{name}' added successfully (ID: {new_product['id']}).")

def addToCart(product_id, user):
    products = load_products()
    product = None
    
    for p in products:
        if int(p["id"]) == product_id:
            product = p
            break
    
    if not product:
        print("Product not found.")
        return
    
    if product["stock"] <= 0:
        print("Product out of stock.")
        return
    
    try:
        quantity = int(input(f"Quantity (available: {product['stock']}): "))
        if quantity <= 0:
            print("Quantity must be positive.")
            return
        if quantity > product["stock"]:
            print(f"Only {product['stock']} available.")
            return
    except:
        print("Invalid quantity.")
        return
    
    users = load_users()
    for u in users:
        if u["username"] == user["username"]:
            cart_item = {
                "product_id": product_id,
                "product_name": product["name"],
                "price": product["price"],
                "quantity": quantity,
                "seller_username": product["seller_username"]
            }
            
            found = False
            for item in u["cart"]:
                if item["product_id"] == product_id:
                    item["quantity"] += quantity
                    found = True
                    break
            
            if not found:
                u["cart"].append(cart_item)
            
            save_users(users)
            print(f"Added {quantity} x {product['name']} to cart.")
            return

def removeFromCart(product_id, user):
    users = load_users()
    
    for u in users:
        if u["username"] == user["username"]:
            found = False
            for item in u["cart"]:
                if item["product_id"] == product_id:
                    found = True
                    try:
                        quantity = int(input(f"Remove quantity (current: {item['quantity']}): "))
                        if quantity <= 0:
                            print("Quantity must be positive.")
                            return
                        if quantity >= item["quantity"]:
                            u["cart"] = [i for i in u["cart"] if i["product_id"] != product_id]
                            print("Product removed from cart.")
                        else:
                            item["quantity"] -= quantity
                            print(f"Removed {quantity} from cart.")
                        save_users(users)
                    except:
                        print("Invalid quantity.")
                    return
            
            if not found:
                print("Product not in cart.")
            return

def showCart(user):
    users = load_users()
    
    for u in users:
        if u["username"] == user["username"]:
            if not u["cart"]:
                print("Your cart is empty.")
                return
            
            total = 0
            print("\n--- Your Cart ---")
            for item in u["cart"]:
                item_total = item["price"] * item["quantity"]
                total += item_total
                print(f"ID: {item['product_id']}")
                print(f"Product: {item['product_name']}")
                print(f"Price: ${item['price']:.2f} x {item['quantity']}")
                print(f"Subtotal: ${item_total:.2f}")
                print("-" * 30)
            
            print(f"Total: ${total:.2f}")
            return

def updateProfile(user):
    users = load_users()
    
    for u in users:
        if u["username"] == user["username"]:
            print("\n1. Update Name")
            print("2. Update Email")
            print("3. Update Address")
            print("4. Update Phone")
            print("5. Update Password")
            
            choice = input("Select option: ").strip()
            
            if choice == "1":
                new_name = input("New name: ").strip()
                if new_name:
                    u["name"] = new_name
            elif choice == "2":
                new_email = input("New email: ").strip()
                if new_email:
                    email_exists = any(existing['email'] == new_email and existing['username'] != user['username'] for existing in users)
                    if email_exists:
                        print("Email already exists.")
                        return
                    u["email"] = new_email
            elif choice == "3":
                new_address = input("New address: ").strip()
                u["address"] = new_address
            elif choice == "4":
                new_phone = input("New phone: ").strip()
                u["phone"] = new_phone
            elif choice == "5":
                new_password = input("New password: ").strip()
                if new_password:
                    u["password"] = new_password
            else:
                print("Invalid option.")
                return
            
            save_users(users)
            print("Profile updated.")
            return

def adminDashboard(user):
    while True:
        print(f"\nWelcome {user['name']} (Admin)")
        print("1. Show all products")
        print("2. Update Profile")
        print("3. Show all users")
        print("4. Delete product")
        print("5. Delete user")
        print("6. Logout")

        choice = input("Enter Choice: ").strip()

        if choice == "1":
            showAllProducts()
        elif choice == "2":
            updateProfile(user)
        elif choice == "3":
            showAllUsers()
        elif choice == "4":
            try:
                product_id = int(input("Product ID: "))
                deleteProduct(product_id)
            except:
                print("Invalid ID.")
        elif choice == "5":
            username = input("Username: ").strip()
            deleteUser(username)
        elif choice == "6":
            logout(user)
            break
        else:
            print("Invalid Input")

def sellerDashboard(user):
    while True:
        print(f"\nWelcome {user['name']} (Seller)")
        print("1. Show my products")
        print("2. Update Profile")
        print("3. Delete product")
        print("4. Add product")
        print("5. Logout")

        choice = input("Enter Choice: ").strip()

        if choice == "1":
            showAllSellerProducts(user)
        elif choice == "2":
            updateProfile(user)
        elif choice == "3":
            try:
                product_id = int(input("Product ID: "))
                deleteProduct(product_id, user)
            except:
                print("Invalid ID.")
        elif choice == "4":
            addProduct(user)
        elif choice == "5":
            logout(user)
            break
        else:
            print("Invalid Input")

def customerDashboard(user):
    while True:
        print(f"\nWelcome {user['name']} (Customer)")
        print("1. Show all products")
        print("2. Update Profile")
        print("3. Add to cart")
        print("4. Remove from cart")
        print("5. Show cart")
        print("6. Logout")

        choice = input("Enter Choice: ").strip()

        if choice == "1":
            showAllProducts()
        elif choice == "2":
            updateProfile(user)
        elif choice == "3":
            try:
                product_id = int(input("Product ID: "))
                addToCart(product_id, user)
            except:
                print("Invalid ID.")
        elif choice == "4":
            try:
                product_id = int(input("Product ID: "))
                removeFromCart(product_id, user)
            except:
                print("Invalid ID.")
        elif choice == "5":
            showCart(user)
        elif choice == "6":
            logout(user)
            break
        else:
            print("Invalid Input")

def signIn():
    email = input("Email: ").strip()
    password = input("Password: ").strip()

    users = load_users()
    
    for user in users:
        if user["email"] == email and user["password"] == password:
            print("Login successful")
            if user["role"] == "admin":
                adminDashboard(user)
            elif user["role"] == "seller":
                sellerDashboard(user)
            else:
                customerDashboard(user)
            return
    
    print("Login failed")

def signUp():
    name = input("Name: ").strip()
    email = input("Email: ").strip()
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    
    try:
        age = int(input("Age: "))
    except:
        print("Invalid age.")
        return
    
    gender = input("Gender: ").strip()
    address = input("Address: ").strip()
    phone = input("Phone: ").strip()
    
    print("Roles: admin, seller, customer")
    role = input("Role: ").strip()
    
    while role not in ["admin", "seller", "customer"]:
        print("Invalid role.")
        role = input("Role: ").strip()

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
        "cart": []
    }
    
    users = load_users()

    for user in users:
        if user["username"] == username:
            print("Username exists.")
            return
        if user["email"] == email:
            print("Email exists.")
            return
        
    users.append(new_user)
    save_users(users)
    print("Account created. Sign in now.")

def mainMenu():
    initializeFiles()

    while True:
        print("\nMH-Mall")
        print("1. Sign In")
        print("2. Sign Up")
        print("3. Exit")

        choice = input("Choice: ").strip()

        if choice == "1":
            signIn()
        elif choice == "2":
            signUp()
        elif choice == "3":
            print("Goodbye")
            break
        else:
            print("Invalid choice")

mainMenu()