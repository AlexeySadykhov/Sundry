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
