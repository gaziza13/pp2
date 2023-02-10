from itertools import permutations

def perm(s):
    x = [''.join(p) for p in permutations(s)]
    return x

y = input()
print(perm(y))
