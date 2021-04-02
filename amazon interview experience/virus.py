# https://www.geeksforgeeks.org/amazon-interview-experience-for-sde-1-6-months-experienced-off-campus/?ref=rp

# Python3 program for the above approach
def countSteps(n):
	
	count = 0
	while (n > 1):
		count += 1

		# num even, divide by 2
		if (n % 2 == 0):
			n //= 2

		# num odd, n%4 == 1
		# or n==3(special edge case),
		# decrement by 1
		elif (n % 4 == 1 or n == 3):
			n -= 1

		# num odd, n%4 == 3, increment by 1
		else:
			n += 1

	return count

# Driver code
if __name__ == "__main__":
	
	n = 15

	# Function call
	print(countSteps(n))

# This code is contributed by chitranayal
