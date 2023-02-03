def myf(n):
	return lambda a: a*n
myd = myf(2)
print(myd(11))