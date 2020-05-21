def fib(n):
	if n == 1:
		return 1
	else:
		ans = fib(n-1) +fib(n-2)
	return ans
t = int(input())
print(fib(t))
