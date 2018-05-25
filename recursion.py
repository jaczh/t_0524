def powpow(x,n):
	if n < 1:
		return 1
	return x*powpow(x,n-1)


def fibonacci(n):
	if n <= 1:
		return n
	return fibonacci(n-1)+fibonacci(n-2)

def BinarySearch(arr,start,end,x):
    mid = (start+end)/2
    if start > end:
        return -1
    elif x == arr[mid]:
        return mid
    elif x < arr[mid]:
        return BinarySearch(arr,start,mid-1,x)
    elif x > arr[mid]:
        return BinarySearch(arr,mid+1,end,x)
    return -1

#---------Binary Search------------------
A = [1,2,3,4,5,7,8,9,10]
x = 5
result = BinarySearch(A,0,len(A)-1,x) 
print(x, 'is in index ',result)
#----------------------Math------------------
base = 3
n = 10
po = powpow(base,n)
print('powpow result: ',po,pow(base,n))
print('---------------------------')
fib = fibonacci(n)
print('fibonacci result:', fib)

#test branch
