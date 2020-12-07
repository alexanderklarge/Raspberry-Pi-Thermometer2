### Imports
import mysql.connector
from mysql.connector.constants import ClientFlag
from src import config

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
#config['database'] = 'testdb'
cursor = connection.cursor()


### Creating SQL database
cursor.execute("CREATE TABLE temperature_and_humidity3 ("
                "timestamp DATETIME,"
                "temperature FLOAT,"
                "humidity FLOAT)")
connection.commit()