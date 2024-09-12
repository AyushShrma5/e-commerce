from db_connection import get_db_connection

class Customer:
    def add_customer(name, email):
        mydb = get_db_connection()
        cursor = mydb.cursor()
        cursor.execute("INSERT INTO customers (name, email) VALUES (%s, %s)", 
                           (name, email))
        mydb.commit()
    
    def list_customer():
        mydb = get_db_connection()
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM customers")
        for row in cursor.fetchall():
            print(row)
        mydb.commit()
    
    def remove_customer(customer_id):
        mydb = get_db_connection()
        cursor = mydb.cursor()
        cursor.execute("DELETE FROM customers WHERE id = %s", (customer_id,))
        mydb.commit()

