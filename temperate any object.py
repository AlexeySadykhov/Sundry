def temperate(start, length):
    array = [start]
    for i in range(length):
        start *= pow(2, 1 / 12)
        array.append(start)
    return array


def save(filename, data):
    file = open(filename + '.txt', 'w')
    for item in data:
        file.write(str(item) + '\n')
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
