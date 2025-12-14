import mysql.connector

conn = mysql.connector.connect(host = "localhost", 
                               user = "root",
                               password = "root",
                               database = "inventory_db" ) # again don't need to use "use inventory_db" as it is passed here

n = conn.cursor()

def add_product(name,quantity,price):

    query_1 = "insert into products(name,quantity, price) values (%s,%s,%s)"

    try:

        n.execute(query_1,(name,quantity,price))

        conn.commit()

        return "Added successfully"

    except mysql.connector.Error as err:
        
        return f"Error: {err}"
   

def update_product(id,quantity,price):

    query = "select * from products where id = %s"

    try:

        n.execute(query,(id,))

        result = n.fetchone()

    except mysql.connector.Error as err:
        
        return f"Error: {err}"

    if not result:
    
        return "Product not found!"

    query_2 = "update products set quantity = %s, price = %s where id = %s"

    try :

        n.execute(query_2,(quantity,price,id))

        conn.commit()

        return "Updated successfully"

    except mysql.connector.Error as err:
        
        return f"Error: {err}"

def delete_product(id):

    query = "select * from products where id = %s"

    try:

        n.execute(query,(id,))

        result = n.fetchone()

    except mysql.connector.Error as err:
        
        return f"Error: {err}"

    if not result:

        return "Product not found!"

    query_3 = "delete from products where id = %s"

    try :

        n.execute(query_3, (id,))

        conn.commit()

        return "Deleted successfully"

    except mysql.connector.Error as err:
        
        return f"Error: {err}"

def fetch_products():

    try:

        n.execute("SELECT * FROM products")

        return n.fetchall()
    
    except mysql.connector.Error as err:

        return f"Error: {err}"

