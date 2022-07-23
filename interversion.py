def interverse(l, nth):
    if nth > len(l)-1:
        print("Error. Nth argument must be less to number of list's elements")
        input()
        exit(1)

    def group(lst, n):
        return [lst[i:i + n] for i in range(0, len(lst), n)]


    def replace(lst):
        g_l = group(lst, len(lst)//2)
        g_l[0].reverse()
        for x, y in zip(g_l[0], g_l[1]):
            array.append(x)
            array.append(y)


    array = []
    i = 1
    while i <= nth:
        if len(l) % 2 == 0:
            array.clear()
            replace(l)
            l = array[:]
        else:
            array.clear()
            c = len(l)//2
            array.append(l[c])
            l.pop(c)
            replace(l)
            l = array[:]
        i += 1

    return l

print(interverse([1, 2, 3, 4, 5, 6], 1))
