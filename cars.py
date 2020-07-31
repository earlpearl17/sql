# Create a database called "cars", and table called "inventory"

# import the SQLite3 library
import sqlite3

# create a connection to the newly created "cars" database
conn = sqlite3.connect("cars.db")

# create a cursor to execute SQL commands
cursor = conn.cursor()

# use the cursor to create the "inventory" table
cursor.execute("""CREATE TABLE inventory
                (make TEXT, model TEXT, quantity INT)
                """)

# close the database connection
conn.close()

