import re
def x(text):
    y = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', y).lower()

text=input()
print(x(text))