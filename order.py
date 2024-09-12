from db_connection import get_db_connection
from mysql.connector import Error

class Order:
    def place_order(customer_id, order_date, product_id, quantity, price):
        mydb = get_db_connection()
        cursor = mydb.cursor()
        cursor.execute("INSERT INTO orders (customer_id, order_date) VALUES (%s, %s)", 
                           (customer_id, order_date))
        mydb.commit()
        order_id = cursor.lastrowid
        cursor.execute("INSERT INTO order_items (order_id, product_id, quantity, price) VALUES (%s, %s, %s, %s)", 
                           (order_id, product_id, quantity, price))
        mydb.commit()
    
    def list_order_details():
        mydb = get_db_connection()
        if mydb is None:
            print("Database connection failed.")
            return

        cursor = mydb.cursor()
        query = """
                SELECT 
                o.id AS order_id,
                c.name AS customer_name,
                c.email AS customer_email,
                o.order_date,
                oi.product_id,
                p.name AS product_name,
                oi.quantity,
                oi.price
            FROM 
                orders o
            JOIN 
                customers c ON o.customer_id = c.id
            JOIN 
                order_items oi ON o.id = oi.order_id
            JOIN 
                products p ON oi.product_id = p.id
            ORDER BY 
                o.id, oi.product_id
        """
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(f"Order ID: {row[0]}, Customer Name: {row[1]}, Customer Email: {row[2]}, "
                  f"Order Date: {row[3]}, Product ID: {row[4]}, Product Name: {row[5]}, "
                  f"Quantity: {row[6]}, Price: {row[7]}")
        mydb.commit()
    

#customer_id = input("Enter customer id: ")
#order_date = input("Enter order date: ")
#product_id = int(input("Enter product id: "))
#quantity = int(input("Enter product quantity: "))
#price = float(input("Enter price: "))

#Order.place_order(customer_id, order_date, product_id, quantity, price)