import sqlite3


def initiate_db(id_product, title_product, description, price):
    connection = sqlite3.connect('products_data.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
        id INT PRIMARY KEY,
        title TEXT NOT NULL,        
        description TEXT,    
        price INT NOT NULL    
        );    
        ''')
    check_product = cursor.execute("SELECT * FROM Products WHERE title=?", (title_product,))
    if check_product.fetchone() is None:
        cursor.execute(f'''
        INSERT INTO Products VALUES('{id_product}', '{title_product}','{description}','{price}')
''')
    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('products_data.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    all_products = cursor.fetchall()
    connection.commit()
    connection.close()
    return all_products
