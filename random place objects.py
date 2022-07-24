#####################################################################################################
# The goal of this script is quite simple but really useful.                                        #
# It just creates a virtual axis and puts random points there.                                      #
# If you split a list of these values into several nested lists you can get a random binary matrix. #
# This script has been designed for using in stochastic music composition                           #
# to determine a time points of different events.                                                   #
#####################################################################################################

import random

main_dur = int(input('Enter main duration value:'))
measure_s = input('Enter measure splitting values by space:').split()
measure_l = []
for i, item in enumerate(measure_s):
    measure_s[i] = int(item)
    measure_l.append(measure_s[i])
num_of_bars = int(input('Enter number of bars to generate:'))
num_of_objects = int(input('Enter number of objects to place:'))

dur_count_in_tact = int(main_dur/measure_l[1]*measure_l[0])
dur_count = dur_count_in_tact*num_of_bars

ruler = [-1 for n in range(dur_count)]
rand_index = random.sample([n for n in range(len(ruler))], num_of_objects)
for n in rand_index:
    ruler[n] = ruler[n]*(-1)


def group(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]


beats = group(ruler, dur_count_in_tact)
array = []
for x in beats:
    array.append([measure_l, x])


def parse_to_lisp(array):
    x1 = ' '.join(str(n) for n in array)
    x2 = x1.replace('[', '(')
    x3 = x2.replace(']', ')')
    x4 = x3.replace(',', '')
    return x4


file = open('my_objects_start_points.txt', 'w')
file.write(parse_to_lisp(array))
file.close()
print('File has been saved')
