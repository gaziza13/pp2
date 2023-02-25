def f(n):
    for i in range(1,n):
        yield i*i

for i in f(5):
    print(i)



