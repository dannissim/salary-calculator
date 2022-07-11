import matplotlib.pyplot as plt
import numpy as np

import salary_calculator

x = np.arange(0.0, 50000.0, 10000.0)
y = [salary_calculator.savings(i) for i in x]
z = [salary_calculator.net_income(i) for i in x]
l = [int(y[i] + z[i]) for i in range(len(y))]
plt.plot(x, y, label='Savings')
plt.plot(x, z, label='Net Income')
plt.plot(x, l, label='Total: Savings + Net')
plt.legend(loc='upper left')
plt.xlabel('Gross Salary')
plt.ylabel('₪')
plt.savefig("graph1.png")
plt.show()
