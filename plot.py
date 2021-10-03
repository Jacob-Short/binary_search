import matplotlib.pyplot as plt
import numpy as np


def plot_it():

    x = np.linspace(0, 2, 100)

    fig, ax = plt.subplots() # Creates a figure containing a single axes.
    ax.plot(x, x, label='linear') # Plot some data on the axes.
    ax.plot(x, x**2, label='qaudratic') # Plot more data on the axes...
    ax.plot(x, x**3, label='cubic') # ... and some more.
    ax.set_xlabel('x label') # Add an x label to the axes.
    ax.set_ylabel(' label') # Add an y label to the axes.

    ax.set_title('Simple Plot') # Add a title to the axes.
    ax.legend() # Add a legend.


    plt.show()


plot_it()



