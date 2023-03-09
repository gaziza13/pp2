import os 

with open('111.txt','r') as first, open('A.txt','a') as second:
    for i in first:
        second.write(i)




