# https://www.geeksforgeeks.org/amazon-interview-experience-offcampus-for-sde-1/?ref=rp
def solve(arr):
    arr.sort()
    print (arr)
    n = len(arr)
    ans = []
    for i in range(n-1):
        l = i+1
        r = n-1
        value = arr[i]
        while (l<r):
            sum = arr[l]+arr[r]+value
            if sum>0:
                r = r-1
            elif sum < 0:
                l = l+1
            else:
                ans.append((arr[l],arr[r],value))
                l = l+1
                r = r-1
    return ans
    


if __name__ == "__main__":
    arr = [0, -1, 2, -3, 1]
    print (solve(arr))