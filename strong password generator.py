##########################################################################
# This amazing function can save your data.                              #
# If you need a strong password simply give it a length                  #
# of password you want to have and result will be generated immediately. #
##########################################################################

import random


def generate_password(length):

    letters = ['a', 'b', 'c', 'd', 'e',
               'f', 'g', 'h', 'i', 'j',
               'k', 'l', 'm', 'n', 'o',
               'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z']
    try:
        length = int(length)
    except TypeError:
        exit(1)

    array = []
    i = 0
    while i < length:
        ch = random.randint(0, 1)
        if ch == 1:
            x = random.choice(letters)
            l_ch = random.randint(0, 1)
            if l_ch == 1:
                array.append(x.upper())
            else:
                array.append(x)
        else:
            array.append(random.randint(0, 9))
        i += 1

    result = ''.join(str(x) for x in array)
    return result


print(generate_password(25))
