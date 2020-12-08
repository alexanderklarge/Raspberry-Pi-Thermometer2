# Want to get my database data into a dataframe for plotting
### Imports
import mysql.connector
from mysql.connector.constants import ClientFlag
import pandas as pd
from IPython.display import display
from matplotlib import pyplot as plt
from src import config
from src import functions

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
#config['database'] = 'testdb'
cursor = connection.cursor()

############################################
### Getting a dataframe
#print_all(cursor,connection)
df = select_all(cursor,connection)

df.columns=['Timestamp','Temp','Hum']
df.set_index('Timestamp',inplace=True)

fig = plt.figure()
ax = plt.axes()

ax.plot(df['Temp'])

fig.show()

print(df.head(3))

#print(df['Timestamp'])

#print(df)
