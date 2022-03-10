import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 7), subplot_kw=dict(aspect="equal"))
data = [1.8,8.10,2.70,1.80,48.65,3.60,33.33]

labels = ['0~10%', '10~20%', '20~30%', '30~40%', '40~50%', '50~60%', '60~70%']
colors = ['#fad9c1', '#03396c', '#3b5998', '#63ace5', '#adcbe3', '#e3f0ff']


def func(pct, allvals):
    absolute = int(round(pct / 100. * np.sum(allvals)))
    return "{:.1f}%".format(pct, absolute)


wedges, texts, autotexts = ax.pie(data, colors=colors, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="black"))

plt.setp(autotexts, size=10, weight="bold")
plt.legend(loc='upper left', frameon=False)
plt.show()