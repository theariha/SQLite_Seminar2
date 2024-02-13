import sqlite3

### Task 1.1 SELECT + FETCHONE()
conn = sqlite3.connect('calorie_tracker.db')
cursor = conn.cursor()

try:
    query = """
        SELECT Products.ProductName
        FROM Products
    """
    cursor.execute(query)
    
    ### fetchone 
    result = cursor.fetchone()
    print(" \n------- fetchone results:")
    print(result)
finally:
    conn.close()


### Task 1.2 SELECT + FETCHALL()
conn = sqlite3.connect('calorie_tracker.db')
cursor = conn.cursor()

try:
    query = """
        SELECT Products.ProductName
        FROM Products
    """
    cursor.execute(query)
    
    ### fetchall 
    result = cursor.fetchall()
    print(" \n------- fetchall results:")
    print(result)
finally:
    conn.close()