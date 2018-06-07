import core
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.0, 50000.0, 10000.0)
y = core.savings(x)
z = [core.net_income(i) for i in x]
plt.plot(x, y)
plt.plot(x, z)
plt.savefig("graph.png")
plt.show()
