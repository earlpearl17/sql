"""
Using the COUNT() function, calculate the total number of orders for each make and
model.

Output the car's make and model on one line, the quantity on another line, and then
the order count on the next line.
"""

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("""SELECT o.make, o.model, i.quantity, COUNT(o.make)
                 FROM inventory i INNER JOIN orders o
                 ON i.model = o.model
                 GROUP BY o.model""")

    car_orders = c.fetchall()

    for r in car_orders:
        #print(r[0], r[1], r[2], r[3])
        print("Car: " + r[0] + ", " + r[1])
        print("Quantity: " + str(r[2]))
        print("Orders: " + str(r[3]))