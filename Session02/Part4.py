import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
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
df.index = df["Date"]

investment = 1000
df_new = df.where(df["Jalali_Day"] < 6).loc["2022-08-06":"2022-11-02"].dropna()
open_price_date = df_new["Open"].where(df["Jalali_Day"]==1).dropna()
close_price_date = df_new["Close"].where(df["Jalali_Day"]==5).dropna()
benefit_date = df_new.groupby(["Jalali_WeekofYear"])["Benefit"].sum()
ind = np.array([open_price_date.index[0],*close_price_date.index])
open_price_date.index = ind[1:]
benefit_date.index = ind[1:]
df_investment = pd.DataFrame(index=ind)
df_investment["Open"]= open_price_date
df_investment["Benefit"] = benefit_date
def calculate_remain_investment(benefit,open):
    global investment
    investment = investment*(benefit/open) + investment
    return investment
df_investment["Investment"] = investment
df_investment["Investment"].iloc[1:]= df_investment.iloc[1:].apply(lambda row: calculate_remain_investment(*row[['Benefit', 'Open']]), axis=1)
# Remin money 
print(df_investment["Investment"].loc["2022-11-02"])
# plot line chart
plt.plot(df_investment.index,df_investment["Investment"],label="Sell")
plt.xlabel("Date")
plt.ylabel("Dollar")
plt.legend()
plt.xticks(rotation=45)
plt.show()
