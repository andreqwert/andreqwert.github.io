# A - массив
# x - искомое значение

def linear_search(A, x):
	"""Linear search"""

	answer = 'NotFound'
	for i in range(0, len(A)):
		if A[i] == x:
			answer = i
	return answer


ans = linear_search(['A', 'B', 'C', 'D'], 'E')
print(ans)
