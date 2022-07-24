#####################################################################################################################################
# This example reproduces a basic quantization algorithm, which is usually used in audio processing software                        #
# such as Cubase, Ableton, Pro Tools, etc. When user records his part, for example, some of notes may be a little bit out of tune.  # 
# To simulate this process, “gen” function has been used. It just generates some random values for the main “quantize” function.    #
# The main difference from the standard function of this type is that this one has an option of quantization step.                  #
# It means that user can round off his values not only in 12-tone system. The value of “step” argument is determined by midi cents. #
# That’s why you can round your score parts to quarter tones or even to smaller values.                                             #
#####################################################################################################################################

from random import randint


def gen(q, start, end):
    array = []
    i = 0
    while i < q:
        array.append(randint(start, end))
        i += 1
    array.sort()
    return array


rand_notes = gen(10, 6000, 7200)

print('Random numbers:')
print(rand_notes)


def quantize(lst, step):
    scale = [x for x in range(6000, 7200, step)]

    def nearest_value(items, value):
        found = items[0]
        for item in items:
            if abs(item - value) < abs(found - value):
                found = item
        return found

    return [nearest_value(scale, x) for x in lst]


result = quantize(rand_notes, 50)

print('Result:')
print(result)
