def f(n):
    yield 0
    for i in range(1,n):
        if i % 2 == 0 :
            yield i
        else:
            yield ','

for i in f(int(input())):
    print(i, end =' ')





