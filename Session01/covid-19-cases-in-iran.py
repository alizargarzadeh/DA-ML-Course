import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Load data from a CSV file
df = pd.read_csv(
    "mhmehsp202-official-corona-statistics-provinces25-feb-2020-22-march-2020-fa.csv")

# Create a new DataFrame with specific columns
df_new = pd.DataFrame()
df_new["Tehran"] = df.iloc[8]
df_new["Mashhad"] = df.iloc[11]
df_new["Isfahan"] = df.iloc[4]
df_new["Karaj"] = df.iloc[5]
df_new["Shiraz"] = df.iloc[17]
df_new["Tabriz"] = df.iloc[1]
df_new["Qom"] = df.iloc[19]
df_new["Ahvaz"] = df.iloc[13]
df_new["Kermanshah"] = df.iloc[22]
df_new["Urmia"] = df.iloc[2]

# Generate and display a plot
plt.plot(df_new["Tehran"].iloc[1:], label="Tehran")
plt.plot(df_new["Mashhad"].iloc[1:], label="Mashhad")
plt.plot(df_new["Isfahan"].iloc[1:], label="Isfahan")
plt.plot(df_new["Karaj"].iloc[1:], label="Karaj")
plt.plot(df_new["Shiraz"].iloc[1:], label="Shiraz")
plt.plot(df_new["Tabriz"].iloc[1:], label="Tabriz")
plt.plot(df_new["Qom"].iloc[1:], label="Qom")
plt.plot(df_new["Ahvaz"].iloc[1:], label="Ahvaz")
plt.plot(df_new["Kermanshah"].iloc[1:], label="Kermanshah")
plt.plot(df_new["Urmia"].iloc[1:], label="Urmia")
plt.xticks(rotation=45)
plt.xlabel("Days")
plt.ylabel("Total Coronavirus Cases")
plt.title("Total Cases in 10 Cities")
plt.legend()
plt.show()
