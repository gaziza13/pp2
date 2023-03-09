import os

with open(r'111.txt') as a:
    lines = len(a.readlines())
    print('total number of lines:',lines)