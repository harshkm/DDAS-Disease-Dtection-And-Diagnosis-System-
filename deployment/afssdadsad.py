import numpy as np
import matplotlib.pyplot as plt
time=np.arange(0, 10, 0.1)
y=np.sin(time)
plt.plot(time,y)
plt.show()

data = data.drop(labels="name", axis=1)