import matplotlib.pyplot as plt
import numpy as np

xs = np.linspace(0, 100, 100)
ys = np.cos(0.1 * xs)

plt.plot(xs, ys, label="$t_ab$")
plt.legend()
plt.show()
