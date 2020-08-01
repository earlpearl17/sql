"""
Prompt the user whether they would like to perform an aggregation (AVG, MAX,
MIN, or SUM) or exit the program altogether.
"""
import sqlite3

# prompt = """Would you like to perform an aggregation (AVG, MIN, MAX or SUM)?
# Or, type 'exit' to exit: """
prompt = """
Select the operation you would like to perform:
1. Average (AVG)
2. Minimum (MIN)
3. Maximum (MAX)
4. Sum (SUM)
5. Exit
"""


# prompt the user to perform an aggregation (AVG,MIN,MAX,SUM) or exit
while True:
    ans = input(prompt)
    if ans.lower() == 'exit':
        break
    else:
        # generate query
        query = 'SELECT ' + ans.upper() + '(number) from numbers'
        #print(query)
        # connect to the database
        with sqlite3.connect("newnum.db") as connection:
            # create a cursor to perform the aggregation
            c = connection.cursor()

            # execute query
            c.execute(query)

            # assign results of query to variable
            res = c.fetchone()[0]

            # display results
            print(f"{res}\n")


  