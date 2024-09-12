from db_connection import get_db_connection

class Product:
    def add_product(name, price, stock):
        mydb = get_db_connection()
        cursor = mydb.cursor()
        cursor.execute("INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)", 
                           (name, price, stock))
        mydb.commit()
    
    def list_products():
        mydb = get_db_connection()
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM products")
        for row in cursor.fetchall():
            print(row)
        mydb.commit()
    
    def remove_product(product_id):
        mydb = get_db_connection()
        cursor = mydb.cursor()
        cursor.execute("DELETE FROM products WHERE id = %s", (product_id,))
        mydb.commit()

