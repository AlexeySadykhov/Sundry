#######################################################################################################################
# This script has been created for music composers. Let us say, if we work with a tempered scale                      #
# it means that our pitch organization obeys to the determined system with its own logic.                             #
# Sometimes composers want to apply these rules to other parameters of the sound, not only to the pitch.              #
# For example, in 12-tone music it was very popular method: some composers used to create a tempered scale of tempos. #
# This utility allows you to use it with anything you want.                                                           #
# You only need to specify a start point of your parameter and a number of iterations you want to get.                #
#######################################################################################################################

def temperate(start, length):
    array = [start]
    for i in range(length):
        start *= pow(2, 1 / 12)
        array.append(start)
    return array


def save(filename, data):
    file = open(f"{filename}.txt", "w")
    for item in data:
        file.write(f"{str(item)}\n")
    file.close()


start_point = float(input('Enter start point:'))
num_of_iter = int(input('Enter number of iterations:'))
result = temperate(start_point, num_of_iter)
print(result)

ans = input('Do you want to save .txt file? (y/n)')
if ans == 'y':
    file_name = input('Enter file name to save:')
    save(file_name, result)
print('Ready')
