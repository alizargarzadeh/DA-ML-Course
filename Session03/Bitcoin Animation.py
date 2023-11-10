import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.animation as animation

df = pd.read_csv("../BTC-USD.csv")
df["Date"] = df["Date"].apply(lambda x: datetime.strptime(x,"%Y-%m-%d"))
fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = ax.plot([], [],"b-",label="Open Price")

def init():
    ax.set_xlim(df["Date"].min(),df["Date"].max())
    ax.set_ylim(df["Open"].min()-500, df["Open"].max()+500)
    ax.set(xlabel="Days", ylabel="Open Price")
    return ln,

def update(frame):
    xdata.append(df["Date"].iloc[frame])
    ydata.append(df["Open"].iloc[frame])
    ln.set_data(xdata, ydata)
    return ln,

ani = animation.FuncAnimation(fig, update,\
                     frames=np.arange(0, 366), init_func=init, blit=True)

plt.title("Bitcon Yearly Open Price")
plt.legend()
# plt.show()

ani.save(filename="../Bitcoin_Open_Price.gif", writer="pillow")
