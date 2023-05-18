import numpy as np
import matplotlib.pyplot as plt
from textwrap import wrap

with open("settings.txt", "r") as f_settings:
    settings = [float(i) for i in f_settings.read().split("\n")]

#get data of voltage through quanization step
data_volt = np.loadtxt("data.txt", dtype = int)*settings[1] 

#get data of time through step of time
data_time = np.array([i*settings[0]*1000 for i in range(len(data_volt))])

#size of graphik
fig, ax = plt.subplots(figsize=(16, 10), dpi = 400)  #count axes in figure 

ax.plot(data_time, data_volt, marker='o', label="V(t)", linewidth = 1, linestyle="solid", markeredgewidth = 1, ms=2, markevery=50)

#max and min for axes
plt.ylim(min(data_volt), max(data_volt))
plt.xlim(min(data_time), max(data_time))

#names of axes
ax.set_ylabel("voltage, V")
ax.set_xlabel("time, sec")

#name of graphik
ax.set_title("\n".join(wrap('Процесс заряда и разряда конденсатора в RC-цепочке', 60)), ha = 'center')

#include grid
plt.grid (True)
ax.grid(which="major", color="k",linewidth=1.8)
ax.grid(which="minor", linestyle=":")
ax.minorticks_on()

plt.annotate("Время зарядки", t.index(max(data_volt)*settings[0]*1000))

#save graphik
fig.savefig("test.png") 
plt.show()