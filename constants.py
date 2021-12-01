def gen():
    yield 1
    yield 2
    yield 3
    yield 4

itr = gen()

print(itr[0])