import matplotlib
import matplotlib.pyplot as plt
from time import sleep
from random import shuffle

matplotlib.use('TkAgg')

# turn on interactive plotting
plt.ion()

y = [i for i in range(100)]
x = [i for i in range(len(y))]

for i in range(50):
    plt.clf()
    plt.bar(x, y)
    plt.draw()
    plt.pause(0.5)
    shuffle(y)
