def BinarySearch(A,n,x,fl):
	low = 0
	high = n-1
	index = -1
	while (low < high):
		mid = (low + high)/2
		if x == A[mid]:
			index = mid
			if fl == 'f':
				high = mid-1
			else:
				low = mid+1
		elif x < A[mid]:
			high = mid-1
		else:
			low = mid+1
	return index

arr = [10,20,20,20,30,40,40,60,70]
num = 40
fir = BinarySearch(arr,len(arr)-1,num,'f')
print('the first', num, 'index is', fir)
if fir == -1:
	print('Not found')
else:
	las = BinarySearch(arr,len(arr)-1,num,'l')
	print('the last', num, 'index is', las)
	print('there are', las-fir + 1, 'numbers of', num)