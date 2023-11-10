import pandas as pd
import matplotlib.pyplot as plt

# Load data from a CSV file
df = pd.read_csv(
    "Weekly_United_States_COVID-19_Cases_and_Deaths_by_State_-_ARCHIVED.csv")

# Generate and display a plot
x = df["end_date"].iloc[:172]
plt.plot(x, df["tot_cases"].iloc[6747:6919], label="New York")
plt.plot(x, df["tot_cases"].iloc[865:1037], label="Los Angeles")
plt.plot(x, df["tot_cases"].iloc[2941:3113], label="Chicago")
plt.plot(x, df["tot_cases"].iloc[1730:1902], label="Miami")
plt.plot(x, df["tot_cases"].iloc[8823:8995], label="Dallas")
plt.plot(x, df["tot_cases"].iloc[692:864], label="Houston")
plt.plot(x, df["tot_cases"].iloc[7439:7611], label="Philadelphia")
plt.plot(x, df["tot_cases"].iloc[2076:2248], label="Atlanta")
plt.plot(x, df["tot_cases"].iloc[1384:1556], label="Washington")
plt.plot(x, df["tot_cases"].iloc[3806:3978], label="Boston")

plt.xticks(ticks=df["end_date"].iloc[:173:6], rotation=45)
plt.ylabel("Cases")
plt.xlabel("10-days moving average")
plt.title("Total Coronavirus Cases")
plt.legend()
plt.show()
