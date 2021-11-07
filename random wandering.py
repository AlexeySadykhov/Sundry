import random
import matplotlib.pyplot as plt


steps = [1, -1]
wandering = []
i = 0
while i != 100:
    i += random.choice(steps)
    wandering.append(i)

plt.plot([n for n in range(len(wandering))],
         wandering)
plt.show()

file = open('random_wandering.txt', 'w')
for x in wandering:
    file.write(str(x)+'\n')
file.close()
print('Done')
