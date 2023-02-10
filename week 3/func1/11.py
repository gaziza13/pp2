def pal(a):
    new = a[::-1]
    if new == a: return True
    else: return False

print(pal(str(input())))
