from product import Product
from customer import Customer
from order import Order

class ECommerceSystem:
    def add_product(self):
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        stock = int(input("Enter product stock quantity: "))
        Product.add_product(name, price, stock)
    
    def list_products(self):
        Product.list_products()
    
    def remove_product(self):
        product_id = int(input("Enter product ID to remove: "))
        Product.remove_product(product_id)
    
    def add_customer(self):
        name = input("Enter customer name: ")
        email = input("Enter email: ")
        Customer.add_customer(name, email)
    
    def list_customers(self):
        Customer.list_customer()
    
    def remove_customer(self):
        Customer_id = int(input("Enter customer ID to remove: "))
        Customer.remove_customer(Customer_id)
    
    def place_order(self):
        customer_id = int(input("Enter customer ID: "))
        order_date = input("Enter order date: ")
        product_id = int(input("Enter product ID: "))
        quantity = int(input("Enter quantity: "))
        price = int(input("Enter price: "))
        Order.place_order(customer_id, order_date, product_id, quantity, price)
    
    def list_orders(self):
        Order.list_order_details()

system = ECommerceSystem()

while True:
    print("\nE-Commerce System")
    print("1. Add Product")
    print("2. Remove Product")
    print("3. List Products")
    print("4. Add Customer")
    print("5. Remove Customer")
    print("6. List Customers")
    print("7. Place Order")
    print("8. List Orders")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        system.add_product()
    elif choice == '2':
        system.remove_product()
    elif choice == '3':
        system.list_products()
    elif choice == '4':
        system.add_customer()
    elif choice == '5':
        system.remove_customer()
    elif choice == '6':
        system.list_customers()
    elif choice == '7':
        system.place_order()
    elif choice == '8':
        system.list_orders()
    elif choice == '9':
        break
    else:
        print("Invalid choice. Please try again.")
