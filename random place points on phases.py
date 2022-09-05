import random
import sys


def group(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]


def positive_exists(nums):
    last_el = nums[0]
    for i, item in enumerate(nums):
        last_el = nums[i]
        if item > 0:
            return True
    if last_el <= 0:
        return False


def parse_to_lisp(arr):
    s1 = ' '.join(str(item) for item in arr)
    s2 = s1.replace(',', '')
    s3 = s2.replace('[', '(')
    s4 = s3.replace(']', ')')
    return s4


num_of_bars = int(input('Enter number of bars to generate:'))
if num_of_bars <= 0:
    print('Error. Number of bars must be positive number.')
    sys.exit(1)

time_sig = list(map(int, input('Enter time signature splitting values by space:').split()))
if len(time_sig) != 2 or time_sig[0] <= 0 or time_sig[1] <= 0:
    print('Error. Time signature is not correct.')
    sys.exit(1)

max_phase = int(input('Enter max phase duration:'))
if max_phase < 2:
    print('Error. Max phase duration must be >= 2.')
    sys.exit(1)

phases = [x for x in range(1, max_phase + 1)] * num_of_bars
phases.sort()

num_of_imp = int(input('Enter number of impulses you want to place:'))
if num_of_imp <= 0 or num_of_imp > sum(phases):
    print('Error. It is impossible to place these values.')
    sys.exit(1)

phase_filter = input('Do you want to delete unused phases? (y/n)')
if phase_filter != 'y' and phase_filter != 'n':
    print('Error. Answer is not correct.')
    sys.exit(1)

impulses = [1 for i in range(num_of_imp)] + [-1 for j in range(sum(phases) - num_of_imp)]
random.shuffle(impulses)

beats = []
bar = []
ph = 0
for i in range(len(impulses)):
    bar.append(impulses[i])
    if len(bar) == phases[ph]:
        beats.append(bar[:])
        bar.clear()
        ph += 1

if phase_filter == 'y':
    beat_data = list(filter(positive_exists, beats))
else:
    beat_data = beats

bars = list(map(lambda x: [time_sig, x], beat_data))
array = group(bars, num_of_bars)

out_file = input('Enter output file location:')
file = open(out_file, 'w')
file.write(parse_to_lisp(array))
file.close()
print('Done')
