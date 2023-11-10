import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.animation import FuncAnimation

df = pd.read_csv("/Users/alizargarzadeh/Desktop/BTC-USD.csv")
df["Date"] = df["Date"].apply(lambda x: datetime.strptime(x,"%Y-%m-%d"))

refreshPeriod = 10 # in ms
fig, ax = plt.subplots()
ln1, =ax.plot(df["Date"],df["Open"],"b-",label="Open Price")
plt.legend()
ln2 = ax.axhline(df["Open"].min(), ls='-', color='r', lw=1, zorder=10)

def init():
    ax.set_xlim(df["Date"].min(),df["Date"].max())
    ax.set_ylim(df["Open"].min()-500, df["Open"].max()+500)
    ax.set(xlabel="Days", ylabel="Open Price")
    return ln2,

def animate(frame):
    global ln2
    y1 = df["Open"].min()
    y = y1 + frame * 100
    ln2.set_ydata([y,y])
    return ln2,

ani = FuncAnimation(fig, animate,init_func=init,\
                    frames=(int((df["Open"].max() - df["Open"].min())//100)),\
                          interval=refreshPeriod)

plt.title("Bitcon Yearly Open Price")
print(((df["Open"].max() - df["Open"].min())//100) )
plt.legend()
# plt.show()
ani.save(filename="../Bitcoin_line.gif", writer="pillow")
