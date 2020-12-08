import mysql.connector
from mysql.connector.constants import ClientFlag
import numpy as np
import pandas as pd

def print_all(cursor,connection):
    print('Select all from database:')
    cursor.execute('SELECT * FROM testdb.temperature_and_humidity2')
    myresult = cursor.fetchall()
    for x in myresult:
      print(x)
      
def select_all(cursor,connection):
    print('Select all from database:')
    cursor.execute('''SELECT
                        DATE_FORMAT(timestamp, '%Y-%m-%d, %H:%i'),
                        temperature,
                        humidity
                        FROM testdb.temperature_and_humidity3''')
    myresult = cursor.fetchall()
    df = pd.DataFrame(myresult)
    #df.columns = cursor.keys()
    return df