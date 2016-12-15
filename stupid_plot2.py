import matplotlib.pyplot as plt
import numpy as np
from chainconsumer import ChainConsumer
from scipy.interpolate import interp1d

xs = np.linspace(0, 100, 100)
ys = np.cos(0.1 * xs)

plt.plot(xs, ys, label="$t_ab$")
plt.legend()
plt.show()
a = [1, 2, 3, 4]

a = interp1d()
a = ChainConsumer()
