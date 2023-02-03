def recur(k):
	if(k > 0):
		result = k + recur(k - 1)
		print(result)
	else:
		result = 0
	return result
print("\n\nRecursion Example Results")
recur(6)