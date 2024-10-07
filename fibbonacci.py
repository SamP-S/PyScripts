
# functionally printing the fibbonacci sequence
# with no depth protection
def fibb_inf(a, b):
	print (a)
	return fibb_inf(b, a + b)


# functionally printing the fibbonacci sequence
# with max depth recursion protection defined by n
def fibb_finite(a=1, b=1, n=10):
	print(a)
	if n > 1:
		return fibb_finite(b, a + b, n-1)


if __name__ == "__main__":
	DEPTH_PROTECTION = True
	N = 20
	A = 1
	B = 1
    
	if DEPTH_PROTECTION:
		fibb_finite(A, B, N)
	else:
		fibb_inf(A, B)

	print("finished")