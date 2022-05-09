def summa(x, y):
    print('summa')
    a = x + y
    if a > 10:
        print(a, '> 10')
    if a < 10:
        print(a, '< 10')
    return a


def raznost(c, v):
    print('raznost')
    s = c - v
    return s


a = int(input('a: '))
b = int(input('b: '))

print(raznost(a, b))
