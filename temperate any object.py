#######################################################################################################################
# This script has been created for music composers. Let us say, if we work with a tempered scale                      #
# it means that our pitch organization obeys to the determined system with its own logic.                             #
# Sometimes composers want to apply these rules to other parameters of the sound, not only to the pitch.              #
# For example, in 12-tone music it was very popular method: some composers used to create a tempered scale of tempos. #
# This utility allows you to use it with anything you want.                                                           #
# You only need to specify a start point of your parameter and a number of iterations you want to get.                #
#######################################################################################################################

start_point = float(input('Enter start point:'))
num_of_iter = int(input('Enter number of iterations:'))

array = []
array.append(start_point)
i = 0
while i < num_of_iter:
    start_point *= pow(2, 1/12)
    print(start_point)
    array.append(start_point)
    i += 1

ans = input('Do you want to save .txt file? (y/n)')
if ans == 'y':
    filename = input('Enter filename to save:')
    file = open(filename + '.txt', 'w')
    for item in array:
        file.write(str(item)+'\n')
    file.close()
    print('Ready! File has been saved.')
else:
    print('Ready!')
