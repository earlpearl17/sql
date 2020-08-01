"""
Add 100 random integers, ranging from 0 to 100, to a new database called
newnum.db
"""

import sqlite3
import random
from time import sleep

# create a database connection to a new database (newnum.db)
with sqlite3.connect("newnum.db") as connection:
    # using the connection, create a cursor to execute commands on the database
    c = connection.cursor()

    # ensure database table doesn't already exist
    c.execute('DROP TABLE IF EXISTS numbers')

    # create a database table
    c.execute("""CREATE TABLE IF NOT EXISTS numbers
                (number INT)
                """)

    # populate the table using the list of random numbers
    for i in range(100):
        c.execute('INSERT INTO numbers VALUES (?)', (random.randint(0,100),))
    
    # # verify numbers table was populated
    # c.execute('SELECT * FROM numbers')

    # rows = c.fetchall()

    # for r in rows:
    #     print(r[0])
    #     #sleep(1)

# NOT NEEDED, taken care of by 'with' keyword
# commit changes
# close connection