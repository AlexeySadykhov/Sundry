from pandas import Series
from itertools import product

test = {'main': [1594663200, 1594666800],
        'a': [1594663340, 1594663389, 1594663390, 
              1594663395, 1594663396, 1594666472],
        'b': [1594663290, 1594663430, 1594663443, 1594666473]}


def presence(intervals):
  
    def group(lst, n):
        return [lst[i:i + n] for i in range(0, len(lst), n)]

    def prepare(lst):
        for i, item in enumerate(lst):
            if item < intervals['main'][0]:
                lst.pop(i)
                lst.insert(i, intervals['main'][0])
            if item > intervals['main'][1]:
                lst.pop(i)
                lst.insert(i, intervals['main'][1])
        return lst

    a = prepare(intervals['a'])
    b = prepare(intervals['b'])
    a_r = group(a, 2)
    b_r = group(b, 2)
    
    def cross(lst1, lst2):
        s1 = Series([n for n in range(lst1[0], lst1[1])])
        s2 = Series([n for n in range(lst2[0], lst2[1])])
        return Series(list(set(s1).intersection(set(s2)))).size

    array = product(a_r, b_r)
    i = 0
    for n in array:
        i += cross(n[0], n[1])

    return i


print('The amount of the presence of 
      "a" and "b" within the "main":', presence(test), 'seconds')
