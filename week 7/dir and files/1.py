import os

path = 'C://Users//User//Desktop'
print(15*'_')
for i in os.listdir(path):
    if os.path.isdir(os.path.join(path,i)):
        print('directions:',i)

print(15*'_')
for i in os.listdir(path):
    if not os.path.isdir(os.path.join(path,i)):
        print('files:',i)

print(15*'_')
for i in os.listdir(path):
    print('directories and files:',i)


