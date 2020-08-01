"""
Add 100 random integers, ranging from 0 to 100, to a new database called
newnum.db
"""

import sqlite3
from random import randint
from time import sleep

num_list = []

# generate a list of random numbers from 0 to 100
for i in range(0,100):
    num_list.append(randint(0,100))

# now convert to list of tuples
tup_list = [(val,) for val in num_list]

print(num_list)
print(tup_list)

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
    #for num in num_list:
        #c.execute('INSERT INTO numbers VALUES (?)', int(num))
        #print(num)
    #c.executemany('INSERT INTO numbers VALUES (?)', num_list)
    c.executemany("INSERT INTO numbers VALUES (?)", tup_list)

    # verify numbers table was populated
    c.execute('SELECT * FROM numbers')

    rows = c.fetchall()

    for r in rows:
        print(r[0])
        #sleep(1)

# NOT NEEDED, taken care of by 'with' keyword
# commit changes
# close connection