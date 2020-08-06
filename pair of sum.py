#BELOW ARE THE 3 METHODS METHODS TO FIND A PAIR OF SUM OF A GIVE NUMER IN AN ARRAY   

#method_01................................................................................................................

def findPair(A, sum):
   for i in range(len(A) - 1):
       for j in range(i + 1, len(A)):
           if A[i] + A[j] == sum:
              print("Pair found at index", i, "and", j)
A = [8, 7, 5, 2, 5, 3, 1]
sum = 10
findPair(A, sum)

#method_02.................................................................................................................

def findPair(A, sum):
	A.sort()
	(low, high) = (0, len(A) - 1)
		if A[low] + A[high] == sum:		# sum found
			print("Pair found", A[low],"and", A[high])
		if A[low] + A[high] < sum:
			low = low + 1
		else:
			high = high - 1
	print("Pair not found")

A = [8, 7, 2, 5, 3, 1]
sum = 10
findPair(A, sum)

#method_03...................................................................................................................

def findPair(A, sum):
	dict = {}
	for i, e i n enumerate(A):
		if sum - e in dict:
			print("Pair found at index", dict.get(sum - e), "and", i)
		dict[e] = i
	print("Pair not found")

A = [8, 7, 2, 5, 3, 1]
sum = 10
findPair(A, sum)
