# Design Document

**Author**: aramirezrivera

## **Version**

| Version | Changes           |
|---------|-------------------|
| 1       | <ul><li> Initial Design Document</li></ul> |

## **Project Overview**
- This project will be used to create a Python script that will run on a raspberry pi computer to store multiple sensor readings in a SQL database.
- The program will be able to tabulate the stored sensor data and send an email with the graph.

## **2. Design Considerations**

### **2.1 Assumptions**

- The code will be organized using the OOP paradigm.
- The SQL database is installed and running locally on the raspberry pi.
- The execution of the main class will be run as a service in the Linux os.

### **2.3 System Environment**

- The application will be developed with Python3 
- The application will run on a raspberry pi4
- The sensors will be connected to the GPIO pins of the raspberry pi

## **3 Low-Level Design**

![uml_diagram.png](images/uml_diagram.png)
