import mysql.connector
import pandas as pd

# Read Bitcoin price data from a CSV file into a pandas DataFrame
df = pd.read_csv("BTC-USD.csv")
df["Benefit"] = df["Close"] - df["Open"]
df["Tolerance"] = df["High"] - df["Low"]
df = df.dropna()

# Establish a connection to the MySQL database
database = mysql.connector.connect(
    host="127.0.0.1",
    port="3306",
    user="root",
    password="$abc123$")

# Create a cursor to execute SQL queries
cursor = database.cursor()

# Create a new MySQL database and a table within the database to store BTC data
cursor.execute("CREATE DATABASE BTC_USD")
cursor.execute("CREATE TABLE BTC_USD.BTC_TBL (Date DATE,\
                Open FLOAT, Close FLOAT, Benefit FLOAT, Tolerance FLOAT)")
for i in range(df.shape[0]):
    cursor.execute("INSERT INTO BTC_USD.BTC_TBL (Date,Open,Close,Benefit,Tolerance) \
                   VALUES (%s,%s,%s,%s,%s)",
                   [df["Date"].iloc[i],
                       df["Open"].iloc[i], df["Close"].iloc[i],
                       df["Benefit"].iloc[i], df["Tolerance"].iloc[i]])


# Commit the changes to the database
database.commit()

# Close the database connection
database.close()
