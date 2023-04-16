class Admin:
    def __init__(self, username, password):
          self.username = username
          self.password = password

class AdminSystem:
    def __init__(self):
        self.admins = []
        
    def add_admin(self, username, password):
        new_admin = Admin(username, password)
        self.admins.append(new_admin)
        print("New admin added to the system!")
        
    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        for admin in self.admins:
            if admin.username == username and admin.password == password:
                print("Login successful!")
                return 
                admin_system = AdminSystem()
                admin_system.add_admin("admin", "password")
                if admin_system.login():
                    print("login succcessful")
                else:
                    print("login unsucccessful")
     
class FoodItem:
    def __init__(self, name, quantity, price, discount, stock):
        self.food_id = None  # will be generated automatically
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock
        
class RestaurantMenu:
    def __init__(self):
        self.food_items = []
        
    def add_food_item(self, name, quantity, price, discount, stock):
        new_food_item = FoodItem(name, quantity, price, discount, stock)
        new_food_item.food_id = len(self.food_items) + 1  # generate FoodID
        self.food_items.append(new_food_item)
        print("New food item added to the menu!")
        self.display_food_items()
        
    def edit_food_item(self, food_id, name, quantity, price, discount, stock):
        found = False
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                found = True
                food_item.name = name
                food_item.quantity = quantity
                food_item.price = price
                food_item.discount = discount
                food_item.stock = stock
                print("Food item updated!")
                self.display_food_items()
                break
        if not found:
            print("Food item not found in the menu.")
            
    def remove_food_item(self, food_id):
        found = False
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                found = True
                self.food_items.remove(food_item)
                print("Food item removed from the menu!")
                self.display_food_items()
                break
        if not found:
            print("Food item not found in the menu.")
            
    def display_food_items(self):
        print("List of food items in the menu:")
        for food_item in self.food_items:
            print("FoodID:", food_item.food_id)
            print("Name:", food_item.name)
            print("Quantity:", food_item.quantity)
            print("Price:", food_item.price)
            print("Discount:", food_item.discount)
            print("Stock:", food_item.stock)
            print("----------------------")

class User:
    def __init__(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
    
def register(self, name, phone_number, email, address, password):
        new_user = User(name, phone_number, email, address, password)
        self.users.append(new_user)
        print("Registration successful!")

def login(self, email, password):
        for user in self.users:
            if user.email == email and user.password == password:
                print("Login successful!")
                return user
        print("Invalid email or password.")
        return None

def place_order(self, user, items):
        order_items = [self.menu[i-1] for i in items]
        total_price = sum([item.price for item in order_items])
        new_order = {"items": order_items, "total_price": total_price}
        user.orders.append(new_order)
        print("Order placed successfully!")

def order_history(self, user):
        if len(user.orders) == 0:
            print("You have not placed any orders yet.")
        else:
            print("Your order history:")
            for i, order in enumerate(user.orders):
                print(f"Order {i+1}:")
                for item in order["items"]:
                    print(f"\t- {item.name} ({item.quantity}) [INR {item.price}]")
                print(f"Total price: INR {order['total_price']}")

def update_profile(self, user, name=None, phone_number=None, email=None, address=None, password=None):
        if name:
            user.name = name
        if phone_number:
            user.phone_number = phone_number
        if email:
            user.email = email
        if address:
            user.address = address
        if password:
            user.password = password
        print("Profile updated successfully!")

role = input("Are you a user or an admin? ")

if role == "user":
    # User registration
    full_name = input("Enter your full name: ")
    phone_number = input("Enter your phone number: ")
    email = input("Enter your email: ")
    address = input("Enter your address: ")
    password = input("Enter your password: ")
    print("registration Succesfull.")

    # User login
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    print("login successful.")
    menu = RestaurantMenu()
    menu.add_food_item("vegan Burger", "1 piece", 320, 0.1, 15)
    menu.add_food_item("tandoori chicken", "4 pieces", 240, 0.2, 20)
    menu.add_food_item("truffle cake", "1 medium", 900, 0.2, 20)
    menu.display_food_items()


    # User options
    option = input("Select an option:\n1. Place New Order\n2. Order History\n3. Update Profile\n")
    if option == "1":
        u.place_order()
    elif option == "2":
        u.order_history()
    elif option == "3":
        full_name = input("Enter your full name (leave blank if not changing): ")
        phone_number = input("Enter your phone number (leave blank if not changing): ")
        email = input("Enter your email (leave blank if not changing): ")
        address = input("Enter your address (leave blank if not changing): ")
        password = input("Enter your password (leave blank if not changing): ")
        u.update_profile(full_name, phone_number, email, address, password)
    else:
        print("Invalid option")

elif role == "admin":
    admin_system = AdminSystem()
    admin_system.add_admin("admin", "password")
if admin_system.login():
    print("login succcessful")
else:
    print("login unsucccessful")