import os,sys

path = 'C://Users//User//Desktop//labbs//week 7//dir and files//111.txt'
print('exists of path:',os.access(path,os.F_OK))
print('readability:',os.access(path,os.R_OK))
print('writability:',os.access(path,os.W_OK))
print('executability:',os.access(path,os.X_OK))