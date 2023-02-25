def f(n):
    i = 0
    while n >i:
        yield n 
        n-=1

for i in f(int(input())):
    print(i,end=' ')