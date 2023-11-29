def myTest():
    yield 1
    yield 5
    yield 6
    yield 99


a = myTest()
b = myTest()


print(a.__next__())
print(a.__next__())
print(b.__next__())
print(b.__next__())
print(a.__next__())
# it resumes the execution of the generator from where it was paused.
# It continues from the last yield statement, producing the next value in the sequence,
# which is 5. So, the correct output for the mentioned line is 1, not 5.


def fibonacci(maximum):
    a, b = 0, 1
    while a < maximum:
        yield a
        a, b = b, a + b


for i in fibonacci(1000000):
    print(i)
