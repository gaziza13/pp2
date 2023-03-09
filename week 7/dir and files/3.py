import os

path = 'C://Users//User//Desktop//labbs//week 7//dir and files//111.txt'

if os.path.exists(path):
    print(os.path.basename(path))
    print(os.path.dirname(path))




