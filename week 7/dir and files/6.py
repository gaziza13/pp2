import os,string

for i in string.ascii_uppercase:
    with open(i + '.txt','w') as a:
        a.writelines(i)