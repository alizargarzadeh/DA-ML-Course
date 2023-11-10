import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from persiantools.jdatetime import JalaliDate

# Setup
df = pd.read_csv("../BTC-USD.csv")
df.dropna(inplace=True)
df["Jalali"] = pd.to_datetime(df["Date"]).apply(
    lambda x: JalaliDate.to_jalali(x))
df["Jalali_Year"] = df["Jalali"].apply(lambda x: JalaliDate.strftime(x, "%Y"))
df["Jalali_Day"] = df["Jalali"].apply(lambda x: JalaliDate.isoweekday(x))
df["Jalali_WeekofYear"] = df["Jalali"].apply(
    lambda x: JalaliDate.week_of_year(x))
df["Benefit"] = df["Close"] - df["Open"]
df["Tolerance"] = df["High"] - df["Low"]

sum_tolerance_day = df.groupby(["Jalali_Year","Jalali_Day"])["Tolerance"].sum()
# sum_tolerance_day.plot(legend=True)
sum_tolerance_day.plot.bar(legend=True)
plt.ylabel("Dollar")
plt.title("Tolerance of Day")
plt.show()

# Maximum Tolerance Day
print(sum_tolerance_day.idxmax()) 
