# Add 5 rows to the cars.db inventory table

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    cars = [
            ('Ford', 'Mustang', 7),
            ('Ford', 'Explorer', 10),
            ('Ford', 'Bronco', 8),
            ('Honda', 'Civic', 12),
            ('Honda', 'Accord', 9)
            ]

    c.executemany('INSERT INTO inventory VALUES (?, ?, ?)', cars)            