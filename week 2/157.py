def myf(n):
	return lambda a: a * n
my3 = myf(3)
print(my3(11))