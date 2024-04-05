from torch import normal
from torchvision import datasets
import matplotlib.pyplot as plt
from IPython.display import display
mean=0
std=1

samples=normal(mean, std, size=(1, 1000))

plt.hist(samples)
plt.show()

celebs=datasets.CelebA(root='./celeb/', download=True)

print(len(celebs))

print(celebs[0])
print(type(celebs[0]))
display(celebs[0])