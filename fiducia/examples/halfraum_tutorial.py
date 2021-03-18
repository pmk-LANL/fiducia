"""
Hohlraum unfold tutorial
===================================


"""


import numpy as np
import fiducia
import matplotlib.pyplot as plt


############################################################
# Generating some data


dataX = np.arange(10)
dataY = dataX ** 2

############################################################
# Plotting the data


plt.plot(dataX, dataY)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Example data')
plt.show()


