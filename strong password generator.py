##########################################################################
# This amazing script can save your data.                                #
# If you need a strong password simply give it a length                  #
# of the password you want to have and the result                        #
# will be generated immediately.                                         #
##########################################################################

import secrets
import string as s

input_correct = False
pass_length = None
while not input_correct:
    try:
        pass_length = int(input("Enter the length of the password:"))
        if pass_length <= 10:
            print("Error. Password length must be greater then 10.\nTry again.")
        else:
            input_correct = True
    except ValueError:
        print("Error. Not a number.\nTry again.")

chars = ''.join([s.digits, s.ascii_letters, s.punctuation])
print(''.join([secrets.choice(chars) for _ in range(pass_length)]))
