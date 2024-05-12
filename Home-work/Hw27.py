def func(a):
    while a < 99999:
        yield a
        a *= -5
for item in func(-2):
    print(item)

print('_' * 100)


def func_1(a):
    while a < 99999:
        yield a
        a *= 3
for item in func_1(10):
    print(item)