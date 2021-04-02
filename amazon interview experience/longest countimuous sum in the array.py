def solve(arr):
    ans = -float("inf")
    for i in range(1,len(arr)):
        arr[i] = max(arr[i-1]+arr[i],arr[i])
        ans = max(ans,arr[i])
    return ans

if __name__ == "__main__":
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    print (solve(arr))