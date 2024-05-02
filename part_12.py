import numpy as np

x = np.arange(1, 11, 0.5)

y = x**2

for i in range(len(x)):
    print(f"x = {x[i]}, y = {y[i]}")