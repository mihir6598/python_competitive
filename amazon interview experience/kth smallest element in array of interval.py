# Python3 program to implement
# the above approach

# Function to get the Kth smallest
# element from an array of intervals
def KthSmallestNum(arr, n, k):
	
	# Store all the intervals so that it
	# returns the minimum element in O(1)
	pq = []

	# Insert all Intervals into the MinHeap
	for i in range(n):
		pq.append([arr[i][0], arr[i][1]])
	print (pq)
	# Stores the count of
	# popped elements
	cnt = 1

	# Iterate over MinHeap
	while (cnt < k):
		
		# Stores minimum element
		# from all remaining intervals
		pq.sort(reverse = True)
		interval = pq[0]

		# Remove minimum element
		pq.remove(pq[0])

		# Check if the minimum of the current
		# interval is less than the maximum
		# of the current interval
		if (interval[0] < interval[1]):
			
			# Insert new interval
			pq.append([interval[0] + 1,
					interval[1]])

		cnt += 1
		
	pq.sort(reverse = True)
	return pq[0][0] + 1

# Driver Code
if __name__ == '__main__':
	
	# Intervals given
	arr = [ [ 5, 11 ],
			[ 10, 15 ],
			[ 12, 20 ] ]

	# Size of the arr
	n = len(arr)
	
	k = 12
	
	print(KthSmallestNum(arr, n, k))

# This code is contributed by SURENDRA_GANGWAR
