print("mmmmmhhhh yeaaaahhh")

# functionally printing the fibbonacci sequence
# with no depth protection
def fibb_deep(a, b):
	print (a)
	return fibb(b, a + b)
	#if a > 10000:
	#	return a + b
	#else:
	#	return fibb(b, a + b)
fibb_deep(1, 1)


# functionally printing the fibbonacci sequence
# with max depth recursion protection defined by n
def fibb_finite(a=1, b=1, n=10):
	print (a)
	if n > 1:
		return fibb(b, a + b, n-1)

fibb_finite()
