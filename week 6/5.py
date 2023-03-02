import re

text = input()
pattern = '^a.+b$'
x= re.search(pattern,text)
print(x)





