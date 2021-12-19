"""
Problem #1 :
Write a python script to retrieve data from SQL into Excel, and schedule to run the script automatically on everyday at particular time, also send a notification to user once data get retrieved.

"""
# Required library
import pyodbc
import pandas as pd
import os
import datetime
from plyer import notification

# Change working directory 
os.chdir(r"C:\Users\RAM\Desktop\RAM\Python_Problems")

# Create SQL Connection
conn = pyodbc.connect(DRIVER="{SQL Server}", SERVER="RAM-PC", DATABASE="Covid19")

# SQL command to retrieve data
comm = "select * from [world-covid-data] where location = 'India'"

# Read data from SQL using pandas dataframe
df = pd.read_sql_query(comm, conn)

# Export data to excel
df.to_csv("data_"+datetime.datetime.now().strftime('%d-%b-%Y %H%M%S') + ".csv", index=False)

# Send Notification to user
notification.notify(title="Script Status", 
                    message=f"Data has been successfully exported into Excel.\nTotal Rows: {df.shape[0]}\nTotal Columns: {df.shape[1]}", 
                    timeout=10)



