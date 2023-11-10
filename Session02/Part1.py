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

sum_of_week = df.groupby(["Jalali_Year", "Jalali_WeekofYear"])["Benefit"].sum()
sum_of_week.plot(legend=True)
plt.ylabel("Dollar")
plt.title("Benefit of Week")
plt.show()
### Maximum Benefit Week
print(sum_of_week.idxmax()) 
