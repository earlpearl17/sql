# Create the "orders" table to accompany the "inventory" table.

"""Add another table to accompany your "inventory" table called "orders". This table
should have the following fields: "make", "model", and "order_date". Make sure to
only include makes and models for the cars found in the inventory table. Add 15
records (3 for each car), each with a separate order date (YYYY-MM-DD)."""

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    # ensure table is dropped if re-running this script
    c.execute('DROP TABLE IF EXISTS orders')

    # ensure table doesn't already exist
    #c.execute("""CREATE TABLE IF NOT EXISTS orders 
    c.execute("""CREATE TABLE orders 
                    (make TEXT, model TEXT, order_date DATE)
              """)

    # 15 orders, 3 for each type of car
    car_orders = [
        ('Ford', 'Bronco', '2020-08-09'),
        ('Ford', 'Bronco', '2020-10-20'),
        ('Ford', 'Bronco', '2020-09-30'),
        ('Ford', 'Explorer', '2020-08-22'),
        ('Ford', 'Explorer', '2020-08-22'),
        ('Ford', 'Explorer', '2020-08-22'),
        ('Ford', 'Mustang', '2020-08-23'),
        ('Ford', 'Mustang', '2020-11-01'),
        ('Ford', 'Mustang', '2020-12-23'),
        ('Honda', 'Accord', '2020-08-30'),
        ('Honda', 'Accord', '2020-10-30'),
        ('Honda', 'Accord', '2020-10-30'),
        ('Honda', 'Civic', '2020-08-12'),
        ('Honda', 'Civic', '2020-08-28'),
        ('Honda', 'Civic', '2020-09-03')
    ]

    c.executemany('INSERT INTO orders VALUES(?, ?, ?)', car_orders)

    c.execute('SELECT * from orders ORDER BY order_date ASC')

    order_list = c.fetchall()

    for order in order_list:
        print(order[0], order[1], order[2])
        #print("Make: " + r[0], "Model: " + r[1])
        #print("Order Date: " + r[2])
        #print("")
