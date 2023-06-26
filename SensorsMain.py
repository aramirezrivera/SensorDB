import Adafruit_DHT
import time
import psycopg2

# Set the GPIO pin for the sensor
pin = 4

# Set the sensor type
sensor_type = Adafruit_DHT.DHT22

# Connect to the MySQL database
conn = psycopg2.connect(host='localhost', user='pi', password='noletengasmiedo', database='sensordb')

# Create a cursor object
cursor = conn.cursor()

# Create a table to store the sensor data
#cursor.execute('CREATE TABLE sensor_data (timestamp DATETIME, humidity FLOAT, temperature FLOAT)')

# Start a loop to read and store the sensor data
while True:
    # Read the humidity and temperature from the sensor
    hum, temp = Adafruit_DHT.read_retry(sensor_type, pin)
    temp = ((1.8*temp) + 32) #change to farenheight
    # Convert the timestamp to a string
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

    # Insert the sensor data into the database
    cursor.execute('INSERT INTO sensordb.sensor_data (timestamp, humidity, temperature) VALUES (%s, %s, %s)', (timestamp, hum, temp))

    # Commit the changes to the database
    conn.commit()

    # Sleep for 10 seconds
    time.sleep(1800)

# Close the cursor and connection to the database
cursor.close()
conn.close()
#psycopg2.errors.UndefinedTable: relation "sensor_data" does not exist
