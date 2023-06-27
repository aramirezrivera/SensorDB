import psycopg2
import pandas as pd
import matplotlib.pyplot as plt


class graphGenerator:

    def __init__(self, sensorPin):
        self.sensorPin = sensorPin

    def createGraph(self):
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(host='localhost', user='pi', password='noletengasmiedo', database='sensordb')
        cursor = conn.cursor()
        query = "SELECT timestamp, temperature, humidity FROM sensordb.sensor_data"
        cursor.execute(query)
        data = cursor.fetchall()

        df = pd.DataFrame(data, columns=['Timestamp', 'Temperature', 'Humidity'])
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])

        # Plotting the data
        plt.plot(df['Timestamp'], df['Temperature'], color='red', label='Temperature')
        plt.plot(df['Timestamp'], df['Humidity'], color='blue', label='Humidity')

        plt.xlabel('Timestamp')
        plt.ylabel('Measurement')
        plt.title('Temperature and Humidity Data')
        plt.ylim(0, 110)
        plt.legend(loc='lower left')

        # Rotate the x-axis label and adjust spacing
        plt.xticks(rotation='vertical')
        plt.subplots_adjust(bottom=0.2)

        # Display or save the graph
        plt.savefig('temperature_humidity_graph.png')
        plt.cla()


    def emailGraph(self):
        pass
