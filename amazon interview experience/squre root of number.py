# https://www.geeksforgeeks.org/amazon-interview-experience-hyderabad-8-months-experienced/?ref=rp
def solve(n):
    if n == 1:
        return 1
    if n == 0:
        return 1
    if n == 2:
        return 1
    start = 1
    end = n//2
    while True:
        mid = (start + end)//2
        if mid * mid <n:
            if (mid+1)*(mid+1)>n:
                return mid
            start = mid +1
        else:
            end = mid-1

if __name__ == "__main__":
    print (solve(56))