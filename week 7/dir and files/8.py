import os

if os.path.exists('B.txt'):
    os.remove('B.txt')
else:
    print('doesnt exists')
