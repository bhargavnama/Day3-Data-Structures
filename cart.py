class Cart:
    def __init__(self):
        self.cart: list = []
    
    # Add product to the cart
    def addProduct(self, prod:str):
        self.cart.append(prod)
        print(f"Successfully added {prod} to the cart")
    
    # Remove product from the cart
    def removeProduct(self, prod: str):
        if prod in self.cart:
            self.cart.remove(prod)
            print(f"Successfully removed {prod} from the cart")
        else:
            print(f"{prod} is not in the cart")
            
    # Search for a product in the cart
    def search(self, prod: str):
        if prod in self.cart:
            print(f"{prod} is in the cart")
        else:
            print(f"{prod} is not in the cart")
            
    # Display all the products in the cart
    def display(self):
        for prod in self.cart:
            print(prod)

    # Display total number of products 
    def total(self):
        print(f"There are {len(self.cart)} products in the cart")
        
    # Sort the cart items
    def sort_cart(self):
        self.cart.sort()
        print("Products in the cart afetr sorting")
        self.display()
        
    # Clear the cart items
    def empty(self):
        self.cart.clear()
        print(f"Emptied the cart")
        
def printMenu():
    print("-------------------------------------------------------------------------------------------------------------")
    print("1.Add a Product to the cart")
    print("2.Remove a product from the cart")
    print("3.Search for a product in the cart")
    print("4.Display all the products in the cart")
    print("5.Show the total products in the cart")
    print("6.Sert the cart items")
    print("7.EMpty the cart")
    print("8.Exit")
    print("-------------------------------------------------------------------------------------------------------------")
        
cart = Cart()
cond = True
while cond:
    printMenu()
    choice = int(input("Enter your choice: "))
    
    match choice:
        case 1:
            prod = input("Enter product to add: ")
            cart.addProduct(prod)
        case 2:
            prod = input("Enter product to remove: ")
            cart.removeProduct(prod)
        case 3:
            prod = input("Enter product to search: ")
            cart.search(prod)
        case 4:
            print(f"Products in the cart are")
            cart.display()
        case 5:
            cart.total()
        case 6:
            cart.sort_cart()
        case 7:
            cart.empty()
        case 8:
            cond = False
        case _:
            print("Invalid choice. Please try again.")
    
    if not cond: break
        