# Update 2 records in the cars.db inventory table

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("UPDATE inventory SET quantity = 15 WHERE model='Bronco'")
    c.execute("UPDATE inventory SET quantity = 19 WHERE model='Accord'")

    print("\nAFTER CHANGES:\n")

    c.execute("SELECT * FROM inventory")
    
    cars = c.fetchall()

    for car in cars:
        print(car[0], car[1], car[2])