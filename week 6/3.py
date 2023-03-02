import re

text = input()
pattern = '[a-z]+_[a-z]+$'
x= re.search(pattern,text)
print(x)