def f(a,b):
    for i in range(a,b+1):
        yield i*i

for i in f(int(input()),int(input())):
    print(i, end = ' ')



