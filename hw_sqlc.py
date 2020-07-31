# Output only records that are Fords

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("SELECT * FROM inventory WHERE make='Ford'")

    cars = c.fetchall()

    print("\nFords in stock:\n")
    for car in cars:
        print(car[0], car[1], car[2])