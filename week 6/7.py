import re

def z(text):
    x = re.sub('_',' ',text)
    x = x.title()
    x = re.sub(' ','',x)
    return x

text=input()
print(z(text))





