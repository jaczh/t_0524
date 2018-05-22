
def reverse(word):
	print(word,word[0])
	if len(word) <= 1:
		return word
	return reverse(word[1:]) + word[0]

def rev(text):
	i = len(text)-1
	reverseOrder=''
	for letter in range(i+1):
		reverseOrder += text[i]
		i-=1
	return reverseOrder

x = '012345'
print(reverse(x))
y = 'abcd'
print(rev(y))s