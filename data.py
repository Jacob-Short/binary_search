import numpy as np
import matplotlib.pyplot as plt

# rng = np.random.default_rng()

# vals = rng.standard_normal(10)

# more_vals = rng.standard_normal(10)

# fig, ax = plt.subplots() # Creates figure and a single axes

a = [1,2,3,4,5,6]

b = [6,5,4,3,2,1]

plt.plot(a, label='incrementing')
plt.plot(b, label='decrementing')

plt.show()


# print(f'Values: ${vals}')
# print(f'More values: ${more_vals}')