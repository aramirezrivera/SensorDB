import Adafruit_DHT
import time
import psycopg2

class sensorDHT22:

    def __init__(self, pin):
        self.pin = pin

    def read(self):
        # Read the sensor data
        sensor_type = Adafruit_DHT.DHT22
        humidity, temperature = Adafruit_DHT.read_retry(sensor_type, self.pin)
        temperature = ((1.8*temperature) + 32) #change to farenheight
        # Convert the timestamp to a string
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        return temperature, humidity

    def write(self):
        # Write the sensor data
        sensor_type = Adafruit_DHT.DHT22
        temp, humi = self.read()
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        conn = psycopg2.connect(host=config.host, user=config.user, password=config.password, database='sensordb')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO sensordb.sensor_data (timestamp, humidity, temperature) VALUES (%s, %s, %s)', (timestamp, humi, temp))
        conn.commit()
        cursor.close()
        conn.close()