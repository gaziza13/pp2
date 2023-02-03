def func(n):
	return lambda a: a * n
my2=func(2)
my3=func(3)
print(my2(11))
print(my3(11))