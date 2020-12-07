def get_data():
    now = datetime.datetime.utcnow()
    now = now.strftime('%Y-%m-%d %H:%M:%S')
    print(now)
    try:
        humidity,temperature = Adafruit_DHT.read_retry(sensor,pin=2)
        print(temperature)
        print(humidity)
    except RuntimeError as error:
        print('Error getting data')

def get_some_readings(n,delay):
    for x in np.arange(n):
        get_data()
        time.sleep(delay)

def insert_data_to_sql(cursor,connection):
    # Getting values to insert
    try:
        humidity,temperature = Adafruit_DHT.read_retry(sensor,pin=2)
        humidity = round(humidity,2)
        temperature = round(temperature,2)
    except RuntimeError as error:
        temperature = 'Error'
        humidity = 'Error'
    
    now = datetime.datetime.utcnow()
    now_ = now.strftime('%Y-%m-%d %H:%M:%S')
    print(now_)
    insert_query = '''INSERT INTO testdb.temperature_and_humidity3 (timestamp,temperature,humidity)
                        VALUES (%s,%s,%s)'''
    values_tuple = (now_,temperature,humidity)
        
    # Running query
    cursor.execute(insert_query,values_tuple)
    connection.commit()
    print('Successfully inserted')
    print(values_tuple) 

def insert_multiple_readings_into_sql(cursor,connection,n=5,delay=60):
    if n != None:
        for x in np.arange(n):
            insert_data_to_sql(cursor,connection)
            time.sleep(delay)
        
    else:
        while n == None:
            insert_data_to_sql(cursor,connection)
            time.sleep(delay)
       
def select_all(cursor,connection):
    print('Select all from database:')
    cursor.execute('SELECT * FROM testdb.temperature_and_humidity3')
    myresult = cursor.fetchall()
    for x in myresult:
      print(x)