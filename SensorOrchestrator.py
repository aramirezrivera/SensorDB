import sensorDHT22
import time
import threading
import graphGenerator

def sensor1_thread():
    sensorInside1 = sensorDHT22.sensorDHT22(4)

    while True:
        # Store Inside sensor1 data in the sql database
        sensorInside1.write()
        # Sleep for 30 minutes
        time.sleep(1800)
def graph_thread():
    grapher = graphGenerator.graphGenerator(4)
    while True:
        #print("This is the
        grapher.createGraph()
        time.sleep(20)
        #time.sleep(86400)
     
if __name__ =="__main__":

    thread1 = threading.Thread(target=sensor1_thread)
    thread2 = threading.Thread(target=graph_thread)
    thread1.start()
    thread2.start()