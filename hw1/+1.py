def plus_one(x):
    s = ''
    for el in x:
        s += str(el)
    ints = int(s)
    ints += 1
    s = str(ints)
    arr = []
    for i in range(len(s)):
        arr += s[i]
    return arr


print(plus_one([9,9,9,9]))
