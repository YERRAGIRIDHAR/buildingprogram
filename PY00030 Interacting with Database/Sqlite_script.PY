import sqlite3

'''creating a table'''

def create_table():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quntity INTEGER, price REAL)")
    conn.commit()
    conn.close()

'''Inserting the data'''

def insert(item, quantity, price):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)",(item, quantity, price))
    conn.commit()
    conn.close()


'''To view the given data'''

def view():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

'''Deleting a row'''

def delete(item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?", (item,))
    conn.commit()
    conn.close()

'''To update the data in database'''

def update(quantity, price, item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?",(quantity, price, item))
    conn.commit()
    conn.close()
    

    create_table()

# update(10,15,"CoffeeCup")
delete("CoffeeCup")
print(view())

