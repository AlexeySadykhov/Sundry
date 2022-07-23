###############################################################################################
# Easy to use script for children which gives them an opportunity                             #
# to train their basic arithmetic skills. User simply identifies a number of questions        #
# in the test and gives the number he wants to learn.                                         #
# The last field may be empty (in this case all numbers from 1 to 9 will be chosen randomly). #
# In real time script randomly chooses numbers to multiply and reacts on users answers.       #
###############################################################################################

import random
import sys


def calculate(number):
    arg1 = random.randint(2, 9)
    if not number:
        arg2 = random.randint(2, 9)
    else:
        arg2 = number
    return [arg2, arg1, arg1 * arg2]


try:
    count_of_questions = int(input('Enter number of questions:'))
except TypeError:
    print('Error. Argument must be digit.')
    sys.exit(1)
num = input('Enter number you want to train:')
if not num or num.isdigit() is False:
    num = None
else:
    num = int(num)

t = 0
f = 0
i = 0
while i < count_of_questions:
    result = calculate(num)
    question = str(result[0]) + 'x' + str(result[1]) + '?'
    print(question)
    try:
        answer = int(input('Answer:'))
    except TypeError:
        print('Error. Argument must be digit.')
        sys.exit(1)
    if answer == result[2]:
        print('Yes!')
        t += 1
    else:
        print('No')
        print(question.replace('?', '=') + str(result[2]))
        f += 1
    i += 1

print('Count of right answers:', t)
print('Count of wrong answers:', f)
