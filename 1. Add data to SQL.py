### Imports
import mysql.connector
from mysql.connector.constants import ClientFlag
import Adafruit_DHT
import time
import numpy as np
#import pandas as pd
import datetime
from src import config
from src import functions

### Variables and objects
sensor = Adafruit_DHT.DHT22
humidity,temperature = Adafruit_DHT.read_retry(sensor,pin=2)

# Now in timestamp format that should work with SQL
now = datetime.datetime.utcnow()
now = now.strftime('%Y-%m-%d %H:%M:%S')

### SQL connection
config = {
    'user':config.user,
    'password':config.password,
    'host':config.host,
    'client_flags':[ClientFlag.SSL],
    'ssl_ca':'server-ca.pem',
    'ssl_cert':'client-cert.pem',
    'ssl_key':'client-key.pem',
    'database':config.database
    }
connection = mysql.connector.connect(**config)
cursor = connection.cursor()
      
functions.insert_multiple_readings_into_sql(cursor,connection,n=None,delay=600)
#select_all(cursor,connection)    