import psycopg2

'''creating a table'''

def create_table():
    conn=psycopg2.connect("dbname='giri2' user='postgres' password='Giridhar!123' host='localhost' port='5432' " )
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quntity INTEGER, price REAL)")
    conn.commit()
    conn.close()

'''Inserting the data'''

def insert(item, quantity, price):
    conn=psycopg2.connect("dbname='giri2' user='postgres' password='Giridhar!123' host='localhost' port='5432' ")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)", (item, quantity, price))
    conn.commit()
    conn.close()

'''To view the given data'''

def view():
    conn=psycopg2.connect("dbname='giri2' user='postgres' password='Giridhar!123' host='localhost' port='5432' ")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

'''Deleting a row'''

def delete(item):
    conn = psycopg2.connect("dbname='giri2' user='postgres' password='Giridhar!123' host='localhost' port='5432' ")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()

'''To update the data in database'''

def update(quantity, price, item):
    conn=psycopg2.connect("dbname='giri2' user='postgres' password='Giridhar!123' host='localhost' port='5432' ")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    conn.commit()
    conn.close()
    

create_table()
# insert("Grapes", 1, 100)

update(10,230,"Mango")
# delete("Grapes")
print(view())


