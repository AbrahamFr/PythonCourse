
def gen123():
    yield 1
    yield 2
    yield 3

for v in gen123():
    print(v)
print("For loop complete")

g = gen123()
print(g)

print(next(g))
print(next(g))
print(next(g))
print(next(g))
