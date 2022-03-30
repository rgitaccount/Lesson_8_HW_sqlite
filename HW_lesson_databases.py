import sqlite3
from sqlite3 import Error
from random import randint, uniform

products_list = ['Говядина (кроме бескостного мяса)', 'Свинина (кроме бескостного мяса)',
                 'Баранина (кроме бескостного мяса)', 'Куры (кроме куриных окорочков)',
                 'Рыба мороженая неразделанная', 'Масло сливочное', 'Масло подсолнечное',
                 'Молоко питьевое', 'Яйца куриные', 'Сахар-песок', 'Соль поваренная пищевая',
                 'Чай черный байховый', 'Мука пшеничная', 'Хлеб ржаной', 'ржано-пшеничный',
                 'Хлеб и булочные изделия из пшеничной муки', 'Рис шлифованный', 'Пшено',
                 'Крупа гречневая - ядрица', 'Вермишель', 'Картофель', 'Капуста белокочанная свежая',
                 'Лук репчатый', 'Морковь', 'Яблоки']

products = {f: {"price": round(uniform(8.33, 1000.66), 2), "quantity": randint(1, 1000)} for f in products_list}


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn


def create_table(conn, sql_to_create_table):
    try:
        c = conn.cursor()
        c.execute(sql_to_create_table)
        return conn
    except Error as e:
        print(e)
    return conn


def add_products(conn, list_of_products):
    sql = '''INSERT INTO products (product_title, price, quantity)
    VALUES(?, ?, ?)'''
    for i in list_of_products:
        c = conn.cursor()
        c.execute(sql, (i, (list_of_products[i]['price']), list_of_products[i]['quantity']))
        conn.commit()
    return c.lastrowid


def update_product_price(conn, product_id, new_price):
    sql = '''UPDATE products SET price = ? WHERE id = ?'''
    try:
        c = conn.cursor()
        c.execute(sql, (new_price, product_id))
        conn.commit()
    except Error as e:
        print(e)


def update_product_quantity(conn, product_id, new_quantity):
    sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
    try:
        c = conn.cursor()
        c.execute(sql, (new_quantity, product_id))
        conn.commit()
    except Error as e:
        print(e)


def delete_product(conn, id):
    sql = '''DELETE FROM products WHERE id = ?'''
    try:
        c = conn.cursor()
        c.execute(sql, (id,))
        conn.commit()
    except Error as e:
        print(e)


def select_all_products(conn):
    sql = '''SELECT * FROM products'''
    try:
        c = conn.cursor()
        c.execute(sql)
        rows = c.fetchall()

        for r in rows:
            print(r)
    except Error as e:
        print(e)


def select_certain_products(conn, price_less_than, q_greater_than):
    sql = '''SELECT * FROM products WHERE price < ? AND quantity > ?'''
    try:
        c = conn.cursor()
        c.execute(sql, (price_less_than, q_greater_than))
        rows = c.fetchall()

        for r in rows:
            print(r)
    except Error as e:
        print(e)


def select_by_word(conn, word):
    sql = """SELECT * FROM products WHERE product_title LIKE ?"""
    try:
        c = conn.cursor()
        c.execute(sql, ('%'+word+'%',))
        rows = c.fetchall()

        for r in rows:
            print(r)
    except Error as e:
        print(e)


database_name = r'hw.db'
conn = create_connection(database_name)
sql_create_table_products = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR (200) NOT NULL,
price  DOUBLE (8, 2) NOT NULL DEFAULT 0.0,
quantity  INTEGER (5) NOT NULL DEFAULT 0
)
'''

if conn:
    print('Connected successfully')
    #create_table(conn, sql_create_table_products)
    #add_products(conn, products)
    #select_all_students(conn)
    #update_product_price(conn, 1, 55)
    #update_product_quantity(conn, 1, 44)
    #delete_product(conn, 1)
    #select_all_products(conn)
    #select_certain_products(conn, 100, 5)
    select_by_word(conn, "Масло")



