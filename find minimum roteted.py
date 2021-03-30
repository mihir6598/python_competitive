def solve(arr,l,r):
    global minimum
    if l<=r:
        m = (l+r)//2
        minimum = min(arr[m],minimum)
        if arr[m]>=arr[l] and arr[m]>=arr[r]:
            solve(arr,m+1,r)
        elif arr[m]<=arr[l] and arr[m]<=arr[r]:
            solve(arr,l,m-1)
        else:
            solve(arr,l,m)
nums=[1,5,7]
minimum = nums[0]
solve(nums,0,len(nums)-1)
print (minimum)