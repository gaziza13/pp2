def prime(x):
    if x % 2 == 0:
        return False
    else:
        for i in range(2,x):
            if x % i == 0:
                return False
    return True
def filter(list1):
    new = []
    for x in list1:
        if prime(x):
            new.append(x)
    return new
print(filter(([11,3,7,8,4,13])))
