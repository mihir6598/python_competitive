# Python3 implementation to find
# square root of given number
# upto given precision using
# binary search.

# Function to find square root of
# given number upto given precision
def squareRoot(number, precision):

	start = 0
	end,ans = number,1

	# For computing integral part
	# of square root of number
	while (start <= end) :
		mid = int((start + end) / 2)
		
		if (mid * mid == number) :
			ans = mid
			break
		
		# incrementing start if integral
		# part lies on right side of the mid
		if (mid * mid < number) :
			start = mid + 1
			
		
		# decrementing end if integral part
		# lies on the left side of the mid
		else :
			end = mid - 1
		
	# For computing the fractional part
	# of square root upto given precision
	increment = 0.1
	for _ in range(0, precision):
		while (ans * ans <= number):
			ans += increment
		
		# loop terminates when ans * ans > number
		ans = ans - increment
		increment = increment / 10
	
	return ans

# Driver code
print(round(squareRoot(50, 3), 4))
print(round(squareRoot(10, 4), 4))
	
# This code is contributed by Smitha Dinesh Semwal.
