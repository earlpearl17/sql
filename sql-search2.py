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
   
    if ans in set(["1","2","3","4"]):

        operation = {1: 'avg', 2: 'min', 3: 'max', 4: 'sum'}[int(ans)]
        # generate query
        #query = 'SELECT ' + ans.upper() + '(number) from numbers'
        #query = 'SELECT ' + operation + '(number) from numbers'
        #print(query)
        # connect to the database
        with sqlite3.connect("newnum.db") as connection:
            # create a cursor to perform the aggregation
            c = connection.cursor()

            # execute query
            #c.execute(query)
            c.execute(f"SELECT {operation}(number) from numbers")

            # assign results of query to variable
            #res = c.fetchone()[0]
            res = c.fetchone()

            # display results
            #print(f"{res}\n")
            print(operation + ": %.2f" % res[0])
            #print(f"{operation} ")

    elif ans == "5":
        break      
    else:
        continue  
  