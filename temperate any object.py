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
