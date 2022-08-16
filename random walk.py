################################################################
# It is just a simple random walk generator.                   #
# Use it if you want to see beautiful pictures of random walk, #
# which sometimes looks like a cryptocurrency rate =).         #
################################################################

import random
import matplotlib.pyplot as plt


steps = [1, -1]
walk = []
i = 0
while i != 100:
    i += random.choice(steps)
    walk.append(i)

plt.plot([n for n in range(len(walk))],
         walk)
plt.show()

ans = input('Would you like to save a text file? (y/n)')
if ans == 'y':
    file = open('random_walk.txt', 'w')
    for x in walk:
        file.write(f"{str(x)}\n")
    file.close()
print('Done')
