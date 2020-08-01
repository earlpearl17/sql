"""
Finally output the car's make and model on one line, the quantity on another line,
and then the order_dates on subsequent lines below that.
"""

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("""SELECT i.make, i.model, i.quantity, o.order_date
                 FROM inventory i, orders o
                 WHERE i.model = o.model
                 ORDER BY order_date""")

    # c.execute("""SELECT i.make, i.model, i.quantity, o.order_date
    #              FROM inventory i, orders o
    #              WHERE i.model = o.model
    #              #WHERE i.make = o.make
    #              #AND   o.model = o.model
    #              ORDER BY order_date""")

    # c.execute("""SELECT inventory.make, inventory.model,
    #         inventory.quantity, orders.order_date FROM inventory INNER JOIN orders
    #         ON inventory.model = orders.model""")

    car_orders = c.fetchall()

    for r in car_orders:
        #print("Make: " + r[0], "Model: " + r[1])
        print("Car: " + r[0] + ", " + r[1])
        print("Quantity: " + str(r[2]))
        print("Order Date: " + r[3])
        print("")