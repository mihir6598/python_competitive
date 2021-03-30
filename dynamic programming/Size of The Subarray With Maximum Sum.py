def solve(arr):
    dp = [(0,0) for i in range(len(arr))]
    dp[0] = (arr[0],1)
    ans = 0
    m = arr[0]
    for i in range(1,len(arr)):
        if dp[i-1][0]+arr[i]>arr[i]:
            dp[i] = (dp[i-1][0]+arr[i],dp[i-1][1]+1)
        else:
            dp[i] = (arr[i],1)
        if ans<dp[i][0]:
            ans = dp[i][0]
            m = dp[i][1]
    return m

def solve2(arr):
    count = 1
    ans = 0
    m = arr[0]
    for i in range(1,len(arr)):
        if arr[i-1]+arr[i]>arr[i]:
            arr[i] = arr[i-1]+arr[i]
            count = count + 1
        else:
            count = 1
        if m<arr[i]:
            ans = count
            m = arr[i]
    return ans

if __name__ == "__main__":
    arr = [ -2, -3, 4, -1, -2, 1, 5, -3 ]
    print (solve2(arr))