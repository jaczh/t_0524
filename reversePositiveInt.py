def reverse(x):
	rev = 0
	while(x>0):
		remainer = x%10
		rev = rev*10+remainer
		x = x/10
	return rev

num = 12005
print(num)
print'reverse:', reverse(num)
