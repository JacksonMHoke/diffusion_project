from torch import randn_like
from torch import tensor
from torch import normal
import matplotlib.pyplot as plt
mean=0
std=1

samples=normal(mean, std, size=(1, 1000))

plt.hist(samples)
plt.show()