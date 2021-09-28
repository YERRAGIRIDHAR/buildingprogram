import mysql.connector

def create_table():
    conn = mysql.connector.connect(
    user="ardit700_student", 
    password = "ardit700_student", 
    host="108.167.140.122", 
    database = "ardit700_pm1database")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quntity INTEGER, price REAL)")
    conn.commit()
    conn.close()

'''Inserting the data'''

def insert(item, quantity, price):
    conn=mysql.connector.connect(
    user="ardit700_student", 
    password = "ardit700_student", 
    host="108.167.140.122", 
    database = "ardit700_pm1database")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)", (item, quantity, price))
    conn.commit()
    conn.close()

'''To view the given data'''

def view():
    conn=mysql.connector.connect(
    user="ardit700_student", 
    password = "ardit700_student", 
    host="108.167.140.122", 
    database = "ardit700_pm1database")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

'''Deleting a row'''

def delete(item):
    conn = mysql.connector.connect(
    user="ardit700_student", 
    password = "ardit700_student", 
    host="108.167.140.122", 
    database = "ardit700_pm1database")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()

'''To update the data in database'''

def update(quantity, price, item):
    conn=mysql.connector.connect(
    user="ardit700_student", 
    password = "ardit700_student", 
    host="108.167.140.122", 
    database = "ardit700_pm1database")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    conn.commit()
    conn.close()
    

create_table()
insert("Mango", 10, 150)

# update(10,230,"Mango")
# delete("Grapes")
print(view())


